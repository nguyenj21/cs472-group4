#!/usr/bin/python
import json
import requests
import csv
from datetime import datetime, timedelta, date; # Used for recording date of file touch

import os

if not os.path.exists("data"):
 os.makedirs("data")

# Arrays for touched source files
gitFiles = []; # File array
gitAuthors = []; # Author array
gitDates = []; # Date array

# GitHub Authentication function
def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lstTokens)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        pass
        print(e)
    return jsonData, ct

# @dictFiles, empty dictionary of files
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter

    try:
        # loop though all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            commitsUrl = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            # break out of the while loop if there are no more commits in the pages
            if len(jsonCommits) == 0:
                break
            # iterate through the list of commits in  spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)

                # Get author name and dates from repo
                gitAuthor = shaDetails['commit']['author']['name'];
                gitDate = shaDetails['commit']['author']['date'];

                # Date when repo was created
                repoCreationDate = datetime(2015, 6, 17);

                filesjson = shaDetails['files']

                for filenameObj in filesjson:
                    filename = filenameObj['filename']

                    # Check if touched file is source then add to array
                        # File extensions for source files
                    sourceFiles = ['.c', '.cpp', '.kt', 'java'];
                        # Check if current file is source by checking file extension
                    if any(filename.endswith(ext) for ext in sourceFiles):
                        # Add file name, author name, and date to respective array
                            # Add file name to array
                        gitFiles.append(filename);
                            # Add author name to array
                        gitAuthors.append(gitAuthor);
                            # Add date to array
                                # Get correct format for date of touched file
                        fileTouchDate = datetime.strptime(gitDate, '%Y-%m-%dT%H:%M:%SZ');
                                # Get time passed from start of repo to date of touched file
                        timePassed = fileTouchDate - repoCreationDate;
                                # Get week number when file was touched
                        fileTouchWeek = timePassed.days / 7;
                                # Add week number to array
                        gitDates.append(fileTouchWeek);

                        dictfiles[filename] = dictfiles.get(filename, 0) + 1
                        print(filename)

            ipage += 1
    except:
        print("Error receiving data")
        exit(0)
# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = [""]

dictfiles = dict()
countfiles(dictfiles, lstTokens, repo)
print('Total number of files: ' + str(len(dictfiles)))

file = repo.split('/')[1]
# change this to the path of your file
fileOutput = 'data/file_' + file + '.csv'
rows = ["Filename", "Touches"]
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)

bigcount = None
bigfilename = None
for filename, count in dictfiles.items():
    rows = [filename, count]
    writer.writerow(rows)
    if bigcount is None or count > bigcount:
        bigcount = count
        bigfilename = filename
fileCSV.close()
print('The file ' + bigfilename + ' has been touched ' + str(bigcount) + ' times.')
