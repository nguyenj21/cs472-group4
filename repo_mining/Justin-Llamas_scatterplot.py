import json
import requests
import csv
import matplotlib.pyplot as plt 
import numpy as np 
from datetime import datetime, timedelta, date

import os
# I KNOW I COULD HAVE IMPORTED THE ARRAYS FROM THE PREVIOUS BUT I JUST DIDNT OKAY IM SORRY 
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

    #try:
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

            # ADDED in order to find the author names and the time they worked on it
            start = datetime(2015,6,17)
            authors = shaDetails['commit']['author']['name']
            time = shaDetails['commit']['author']['date']

            filesjson = shaDetails['files']

            for filenameObj in filesjson:
                filename = filenameObj['filename']
                
                # ADDED Check if it is a source file being edited, programming languages found in GitHub
                # kotlin, java, c, c++, and cmake (there isnt a .cmake so idk)
                programmingExtensions = ['.kt', '.java', '.c', '.cpp',]
                if any(filename.endswith(lang) for lang in programmingExtensions):
                    authorsArray.append(authors)
                    filesArray.append(filename)
                    # need to calculate the weeks... had to search the datetime import 
                    newDay = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
                    date = newDay - start
                    weekNumber = date.days / 7
                    timeArray.append(weekNumber)
                    # had to change this = to 0 so then i can number them later 
                    dictfiles[filename] = 0
                    print(filename, "\t\t", authors, "\t\t", time)

        ipage += 1
    #except:
        #print("Error receiving data")
        #exit(0)
# GitHub repo
repo = 'scottyab/rootbeer'

# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = []

dictfiles = dict()
# different arrays used
authorsArray = []
timeArray = []
filesArray = []
colors = []
numberFiles = []
countfiles(dictfiles, lstTokens, repo)

# use this to incorpate different colors for different contributors
author_color_map = {author: i for i, author in enumerate(set(authorsArray))}
colors = [author_color_map[author] for author in authorsArray]

# array in order to change the file names to numbers so that the x-axis is numbers instead of files
fileToNumber = 1
for file in filesArray:
    # if the file was not touched aka not numbered yet give it a number
    if dictfiles[file] == 0:
        dictfiles[file] = fileToNumber
        fileToNumber += 1
    # then add that new number file into numberFiles array for the x-axis
for file in filesArray:
    numberFiles.append(dictfiles[file])

# create the scatter plot
plt.scatter(numberFiles,timeArray,c=colors,alpha=0.5)
plt.ylabel('Weeks')
plt.xlabel('Files')
plt.show()
