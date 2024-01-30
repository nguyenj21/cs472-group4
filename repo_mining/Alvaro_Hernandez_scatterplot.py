
import matplotlib.pyplot as plt
import pickle
from datetime import datetime

# Load the data from the pickle file
with open('dataFromCollectFiles.pkl', 'rb') as file:
    imported_dict = pickle.load(file)

# Function to convert dates to the number of weeks since the earliest commit
def convert_dates_to_weeks(dates, earliest_commit_date):
    weeks = [(datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ') - earliest_commit_date).days // 7 for date in dates]
    return weeks

# Find the earliest commit date
all_dates = [date for stats in imported_dict.values() for date in stats['dates']]
earliest_commit_date = min(all_dates, key=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ'))
earliest_commit_date = datetime.strptime(earliest_commit_date, '%Y-%m-%dT%H:%M:%SZ')

# Prepare data for the scatter plot
authors = []
commit_weeks = []
file_indices = []

file_names = list(imported_dict.keys())  # List of all filenames
file_name_to_index = {name: index for index, name in enumerate(file_names, start=1)}  # Mapping of filenames to indices

for filename, stats in imported_dict.items():
    weeks = convert_dates_to_weeks(stats['dates'], earliest_commit_date)
    commit_weeks.extend(weeks)
    authors.extend(stats['authors'])
    file_indices.extend([file_name_to_index[filename]] * len(weeks))

# Function to assign colors to authors dynamically
def assign_colors(authors):
    unique_authors = list(set(authors))
    num_authors = len(unique_authors)
    colormap = plt.cm.get_cmap('tab20', num_authors)
    author_colors = {author: colormap(i) for i, author in enumerate(unique_authors)}
    return [author_colors[author] for author in authors]

author_colors = assign_colors(authors)

# Create the scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(file_indices, commit_weeks, c=author_colors, s=100)

# Customize the plot
plt.xticks(range(1, len(file_names) + 1))  # Use enumeration for the x-axis labels
plt.xlabel('File Index')
plt.ylabel('Weeks Since Earliest Commit')
plt.title('Commit History by Author')
plt.tight_layout()
# Calculate the number of different authors
unique_authors = set(authors)
num_unique_authors = len(unique_authors)

# Calculate the total number of commits
total_commits = len(authors)

# Calculate the duration of the project in weeks
latest_commit_date = max(all_dates, key=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ'))
latest_commit_date = datetime.strptime(latest_commit_date, '%Y-%m-%dT%H:%M:%SZ')
project_duration_weeks = (latest_commit_date - earliest_commit_date).days // 7

# Print the statistics
print("The total number of authors is:", num_unique_authors)
print("The total number of commits is:", total_commits)
print("The duration of the project in weeks is:", project_duration_weeks)

# Existing code for plot
plt.show()
