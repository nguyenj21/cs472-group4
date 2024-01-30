import json
import requests
import csv
import os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from Johnson_authorsFileTouches import countfiles

if not os.path.exists("data"):
    os.makedirs("data")

# GitHub repo
repo = 'scottyab/rootbeer'

# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise, they will all be reverted and you will have to re-create them
# I would advise creating more than one token for repos with heavy commits
lstTokens = ["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",
              "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",
              "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"]

# initializes dictonary for the files
dictfiles = dict()

# calls countfiles to get the data for scatter plot
dictfiles, weeks_vs_file_variables = countfiles(dictfiles, lstTokens, repo)

# setting a initial date to calculate weeks
beginDay = datetime(2015,6,17)

# calculate the weeks difference and add to y_values
y_values = [
    (datetime.strptime(entry["week"], "%Y-%m-%dT%H:%M:%SZ") - beginDay).days / 7
    for entry in weeks_vs_file_variables
]
# extracts data from weeks vs file variables to put in scatterplot
x_values = [entry["file_variables"] for entry in weeks_vs_file_variables]
authors = [entry["author"] for entry in weeks_vs_file_variables]

# create color for each authors dot
author_color_map = {author: i for i, author in enumerate(set(authors))}
colors = [author_color_map[author] for author in authors]

# create scatter plot
plt.scatter(x_values, y_values, c=colors, cmap='plasma', alpha=0.7)

# add labels and title
plt.xlabel('file')
plt.ylabel('weeks')



# display the plot
plt.show()
