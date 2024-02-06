# Alec Him
# NSHE ID: 2001543593
# CS 472 - 1001
# Git and GitHub Lab - File Touches

import os
import requests
import csv

# Replace token with personalized one
token = "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"

# Detect Source Files function
def is_source_file(file_path):
    source_file_extensions = [".java", ".cpp", ".kt"]
    return any(file_path.lower().endswith(ext) for ext in source_file_extensions)

# Grab's contributors data from github repo
def get_file_contributors(file_path):
    # Github Authentication
    headers = {"Authorization": f"token {token}"}
    request = requests.get(f"https://api.github.com/repos/scottyab/rootbeer/commits", params={"path": file_path}, headers=headers)
    commits = request.json()

    # Dictionary to store all contributors
    contributors = {}

    # For loop to store author and dates in dictionary
    for commit in commits:
        author = commit["commit"]["author"]["name"]
        date = commit["commit"]["author"]["date"]
        if file_path not in contributors:
            contributors[file_path] = []
        contributors[file_path].append({"author": author, "date": date})

    return contributors

# Main
if __name__ == "__main__":
    # Open file path to "file_rootbeer.csv" and reads the data contained
    with open("data/file_rootbeer.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Open new CSV file for writing to
        with open("contributors_data.csv", mode='w', newline='') as output_csv:
            fieldnames = ["File Path", "Author", "Date"]
            writer = csv.DictWriter(output_csv, fieldnames=fieldnames)            

            # Write header to the output CSV file
            writer.writeheader()

            # For loop to go through "file_rootbeer.csv"
            for row in reader:
                file_path = row["Filename"]
                touches = int(row["Touches"])

                # Only calls and stores author and dates based on whether file is a source or not
                if is_source_file(file_path):
                    contributors = get_file_contributors(file_path)

                    for contribution in contributors.get(file_path, []):
                        author = contribution["author"]
                        date = contribution["date"]

                        # Write data to the output CSV file
                        writer.writerow({"File Path": file_path, "Author": author, "Date": date})

                        print(f"Data written for File: {file_path}, Touches: {touches}")