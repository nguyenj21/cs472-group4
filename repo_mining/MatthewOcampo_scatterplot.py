import json;
import requests;
import csv;
import os;
import numpy as np;
import matplotlib.pyplot as ppt

# Get file name, author name, and date arrays from authorsFileTouches script
from MatthewOcampo_authorsFileTouches import gitFiles, gitAuthors, gitDates, dictfiles;

# Arrays for scatterplot
authorColors = [];
gitFileNumbers = [];

# Assign different colors for each author
colorMap = {gitAuthor: i for i, gitAuthor in enumerate(set(gitAuthors))};
authorColors = [colorMap[gitAuthor] for gitAuthor in gitAuthors];

fileNumber = 1;

for touchedFile in gitFiles:
    if dictfiles[touchedFile] == 0:
        dictfiles[touchedFile] = fileNumber;
        fileNumber += 1;

for touchedFile in gitFiles:
    gitFileNumbers.append(dictfiles[touchedFile]);

# Scatter plot for touched files
    # Create actual scatterplot
ppt.scatter(gitFileNumbers, gitDates, c = authorColors, cmap = 'magma', alpha = 0.75);
    # Rename x and y axises
ppt.xlabel('Touched Files');
ppt.ylabel('Weeks');
    # Display scatterplot to user
ppt.show();

