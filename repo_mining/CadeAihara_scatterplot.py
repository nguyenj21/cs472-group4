import json
import requests
import csv

import os
import numpy
from datetime import datetime, timedelta

import matplotlib.pyplot as plt

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
nameArr = []
dateArr = []
fileArr = []
fileNoArr = [0]
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter
    i = 0


    try:
        # loop though all the commit pages until the last returned empty page
        # print(" R U N N I N G ")
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
                filesjson = shaDetails['files']
                author = shaDetails['commit']['author']['name']
                date = shaDetails['commit']['author']['date']
                for filenameObj in filesjson:
                    filename = filenameObj['filename']

                    extensions = [
                        ".java",
                        ".cpp",
                        ".c",
                        ".kt",
                        ".cmake"
                        
                    ]
                    begin = datetime(2015,6,14) # start of proj
                    
                    
                    if any(filename.endswith(x) for x in extensions) :
                        dictfiles[filename] = dictfiles.get(filename, 0) + 1
                        #print(filename + "  -  " + author + "  +  " + date)
                        
                        # print(today)
                        
                        if date != 0:
                            date = datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')
                            #print("hit1")
                            date = (date - begin).days/7 
                            #print("hit2")
                            #print("|")
                            nameArr.append(author)
                            dateArr.append(date)
                            # fileArr.append(filename)
                            
                            if(filename not in fileNoArr) :
                                fileNoArr.append(filename)
                            
                            fileArr.append(fileNoArr.index(filename))
                        # for x in nameArr : print(x)
                        date = 0

                    #author = filenameObj['contributor_names']
                    #dictfiles[author] = dictfiles.get(author, 0) + 1
                    #print(author + " - ")

                    #date = filenameObj['date']
                    #dictfiles[date] = dictfiles.get(date, 0) + 1
                   # print(date)
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
lstTokens = ["bird",
                "cat",
                "dog"]


dictfiles = dict()
countfiles(dictfiles, lstTokens, repo)
# num = 1
# for i in fileNoArr:
#     num += 1
#     plt.scatter(fileArr, dateArr, c=num)
plt.scatter(fileArr, dateArr)
plt.xlabel("File")
plt.ylabel("Weeks")
plt.show()

