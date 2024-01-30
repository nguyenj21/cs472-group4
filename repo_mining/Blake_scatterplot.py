import Blake_authorsFileTouches
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

#Get all the information from the authorsFileTouches script
author_dict, latest_date = Blake_authorsFileTouches.get_authors_file_touches('file_rootbeer.csv')

matplotlib.style.use("dark_background")

# Create subplots with the calculated number of rows and columns
fig, ax = plt.subplots()

ax.set_title("scottyab/rootbeer Author Touches")
ax.set_xlabel("File Number")
ax.set_ylabel("Week")

print(len(author_dict))


colors = plt.cm.rainbow(np.linspace(0, 1, len(author_dict))) #set object of colors to iterate through
for author, color in zip(author_dict, colors):
    x_vals = []
    y_vals = []
    for commit in author_dict[author]:
        x_vals.append(commit['fileNameID'])
        y_vals.append(commit['weeksFromCreation'])
    #Build scatter plot for this author
    ax.scatter(x_vals, y_vals, c=color, marker='o', label=author)
    
# Adjust layout
ax.legend()
plt.tight_layout()
plt.show()