import csv
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

csv_file_path = 'data/file_rootbeer.csv'  # Replace with the actual file path

# Read the CSV file and extract dates
dates = []

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        if len(row) >= 3:
            date_str = row[2]
            try:
                date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
                dates.append(date)
            except ValueError:
                print(f"Skipping invalid date format: {date_str}")

# Find the earliest date
earliest_date = min(dates, default=None)

authorList = []
authors = []
filesTouchedInWeek = dict()
weeks = []
filesUnique = dict()

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if len(row) >= 3:
            filename = row[0]
            author = row[1]
            date_str = row[2]
            date = (datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ') - earliest_date).days // 7

            if author not in authorList:
                authorList.append(author)

            if filename not in filesUnique:
                filesUnique[filename] = len(filesUnique)

            #if date not in weeks:
                #weeks.append(date)

            if date not in filesTouchedInWeek:
                filesTouchedInWeek[date] = [filename]
            else:
                filesTouchedInWeek[date].append(filename)

files = []
for week, fileList in filesTouchedInWeek.items():
    for file in fileList:
        files.append(filesUnique[file])
        weeks.append(week)

#print(authorList)
#print(authors)
#print(files)
#print(weeks)
unique_authors = list(set(authorList))
author_colors = {author: f'C{i}' for i, author in enumerate(unique_authors)}
colors = []
for author in authors:
    colors.append(author_colors[author])
#print(author_colors)
plt.figure(figsize=(10, 6))
plt.scatter(files,weeks, c=weeks, s=1)
plt.xlabel('Files')
plt.ylabel('Weeks')
plt.show()