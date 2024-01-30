import json
import requests
import csv
from datetime import datetime

import os

if not os.path.exists("data"):
 os.makedirs("data")

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
    weeks_vs_file_variables = [] #tuple to store data in scatterplot script

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
                
                # collect authors and dates, uses tuple to store
                commitDetails = []
                namesAuthor = shaDetails['commit']['author']['name']
                touchedDates = shaDetails['commit']['author']['date']
                
                # extracting data from shaDetails dictionary
                filesjson = shaDetails['files']
                for filenameObj in filesjson:
                    filename = filenameObj['filename']

                    # makes sure to only take source files that are specifically touched by including a check
                    fileExtSource = ['.cpp', '.kt', '.java',  '.c']

                    # loop to only take source files
                    for ext in fileExtSource:
                        # make sure the files' names end with ext
                        if filename.endswith(ext):
                            # updates dictionary dictfiles and creates a key with default value 0 before incrementing 1
                            dictfiles[filename] = dictfiles.get(filename, 0) + 1
                            # gets the updated value from filename and dictfiles and assigns to file_variables
                            file_variables = dictfiles[filename]
                            # stores collected data into commit details
                            commitDetails.append((namesAuthor, touchedDates, file_variables))
                            # for loop to store into another tuple for scatterplot data in 2nd script
                            for commitDetail in commitDetails:
                                # storing into weeks vs file variables tuple
                                weeks_vs_file_variables.append({
                                    "week": commitDetail[1],
                                    "file_variables" : commitDetail[2],
                                    "author": commitDetail[0]
                            })
                            # prints the names and touched dates of each file
                            print(f"{filename}\t{namesAuthor}\t{touchedDates}")

            ipage += 1
    except:
        print("Error receiving data")
        exit(0)

    return dictfiles, weeks_vs_file_variables
# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = ["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",
                "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",
                "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"]

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
