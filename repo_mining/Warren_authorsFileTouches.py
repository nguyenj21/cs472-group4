import json
import requests
import csv
from datetime import datetime, timedelta, date
import os
#import numpy
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
    filect = 0
    global commitauthorArray
    commitauthorArray = []
    global commitfilesArray
    commitfilesArray = []
    global committimeArray
    committimeArray = []
    global committimeArrayNum
    committimeArrayNum = []

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

                # to get the author's name and the date of the commits
                committime = shaDetails['commit']['author']['date']
                commitauthor = shaDetails['commit']['author']['name'] 
                
                # set beginning date of project
                projectdatebegin = datetime(2015,6,17)


                filesjson = shaDetails['files']
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    
                    allowed_source_ext = ['.c', 'CMakeLists.txt', '.cpp', '.java', '.kt']
                    if any(filename.endswith(ext) for ext in allowed_source_ext):
                        commitauthorArray.append(commitauthor)
                        commitfilesArray.append(filename)

                        #get correct date conversion
                        collectday = datetime.strptime(committime, '%Y-%m-%dT%H:%M:%SZ') 
                        date = collectday - projectdatebegin
                        weektime = date.days / 7

                        committimeArray.append(weektime)  
                        dictfiles[filename] = dictfiles.get(filename, 0) + 1
                        print(filename, "\t", commitauthor, "\t", committime)
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