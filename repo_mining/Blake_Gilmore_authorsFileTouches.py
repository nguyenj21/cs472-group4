import json
import requests
import os
from dotenv import load_dotenv
import pandas as pd
import datetime

#For initial authentication
def github_auth(url, token):
    jsonData = None
    try:
        headers = {'Authorization': 'Bearer {}'.format(token)}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
    except Exception as e:
        pass
        print(e)
    return jsonData

'''
get_authors_file_touches(csv_name)

input: csv_name containing content from a repo in the form of columns ['filename', 'touches']

output: tuple (author_dict, latest_date) 
author_dict: Python dictionary of the form: 
    Author{
        fileName: name of the file,
        fileNameID: unique ID number of the file (used for scatterplot),
        weeksFromCreation: the number of weeks
    }
latest_date: number of weeks between creation of repo and latest commit
'''
def get_authors_file_touches(csv_name):
    load_dotenv()
    github_token = [os.getenv('token')] #Get token from environment variable

    #Relevant strings to use in the program
    repo = 'scottyab/rootbeer'
    file_path = os.getcwd() + '/cs472-group4/repo_mining/data/file_rootbeer.csv'
    touches_df = pd.read_csv(file_path)#read in csv file

    #Metrics to keep track of in commit
    commitUrl = 'https://api.github.com/repos/' + repo
    created_date = datetime.datetime.strptime(github_auth(commitUrl, github_token[0])['created_at'], '%Y-%m-%dT%H:%M:%SZ') #Get creation date to compare other times to
    latest_date = 0

    #Data to keep track of in commits
    files_dict = {}
    file_count = 0
    authors_dict = {}


    #Loop through all files from the csv
    for filename in touches_df['Filename']:
        ipage = 1
        while True:
            spage = str(ipage)
            #Make a call to Github Repos API to collect information on this file
            commitUrl = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100' + '&path=' + filename
            jsonCommit = github_auth(commitUrl, github_token[0])
            if (len(jsonCommit) == 0):
                break
            
            #Assign unique number to file for later graphing
            files_dict[filename] = file_count
            file_count = file_count+1
            
            #Iterate through all commits of the file
            for commit in jsonCommit:
                #First collect week number and author of the commit
                commit_date = datetime.datetime.strptime(commit['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')
                weeks_from_creation = (commit_date - created_date).days // 7

                #Set latest commit week count
                if (weeks_from_creation > latest_date):
                    latest_date = weeks_from_creation
                    
                author_name = commit['commit']['author']['name']
                
                #in case author has not been found before
                if author_name not in authors_dict:
                    authors_dict[author_name] = [] #set empty list for this and later commits
                    
                authors_dict[author_name].append({
                    'fileName': filename,
                    'fileNameID': files_dict[filename],
                    'weeksFromCreation': weeks_from_creation,
                })
                ipage+=1

    return (authors_dict, latest_date)



        
        
        
        
        