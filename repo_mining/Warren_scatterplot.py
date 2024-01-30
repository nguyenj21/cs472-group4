import numpy as np
import matplotlib.pyplot as plt
from Warren_authorsFileTouches import commitauthorArray, commitfilesArray, committimeArray


# Generate data...
x = np.array(commitauthorArray)
y = np.array(commitfilesArray)
z = np.array(committimeArray)

author_color_map = {author: i for i, author in enumerate(set(x))}
colors = [author_color_map[author] for author in commitauthorArray]
# Plot
plt.ylabel('Weeks')
plt.xlabel('Files')
plt.scatter(y, z, c=colors)
plt.show()