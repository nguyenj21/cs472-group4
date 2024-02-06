# Alec Him
# NSHE ID: 2001543593
# CS 472 - 1001
# Git and GitHub Lab - Scatter Plot

import numpy as np
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

# Function to find unique files
def find_unique_files(csv_file):
    unique_files = set()

    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            file_path = row["File Path"]
            file_name = os.path.basename(file_path).strip()
            unique_files.add(file_name)
    
    return unique_files

# Needed to find where contributors_data.csv would be located
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contributors_data.csv")

unique_files = find_unique_files(file)

# Store data from CSV file dataset in array
data = []

# Open file path to "contributors_data.csv" and reads the data contained
with open(file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Dictionaries
    author_colors = {}
    unique_files_dict = {file_name: idx for idx, file_name in enumerate(unique_files)}
    # Dictionary to store data
    data = {"Weeks": [], "Files": [], "Authors": []}

    # For loop to go through "contributors_data.csv"
    for row in reader:
        # Convert the date string to a datetime object
        date = datetime.strptime(row["Date"], "%Y-%m-%dT%H:%M:%SZ")

        # Define the project start date
        project_start_date = datetime(2015, 6, 14)

        # Calculate the weeks since the project started, with a maximum of 250 weeks
        weeks_since_start = (date - project_start_date).days // 7

        # Extract the file name from the path
        file_path = os.path.basename(row["File Path"])
        file_index = unique_files_dict[file_path]

        # Store data
        data["Files"].append(file_index)
        data["Weeks"].append(weeks_since_start)

        author = row["Author"]

        # Assign a color to the author (using a consistent color for each author)
        if author not in author_colors:
            author_colors[author] = len(author_colors)

        author_color = author_colors[author]
        data["Authors"].append(author_color)

# Scatter plot
scatter = plt.scatter(data["Files"], data["Weeks"], c=data["Authors"], cmap='tab10')
plt.xlabel("File")
plt.ylabel("Weeks")
plt.xticks(np.arange(0, len(unique_files), 2), rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout
plt.gcf().set_size_inches(12, 6)
plt.show()