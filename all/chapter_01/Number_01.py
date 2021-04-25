# Color histogram for a tiny randomly generated image

# import statements
import numpy as np
import matplotlib.pyplot as plt


# Creating a random image and convert it to a 2bit image
rnd_img = np.random.uniform(low=0, high=3, size=(5, 5))
rnd_img = np.uint8(rnd_img)

# Creating a histogram and returning the frequency of each level
hist = np.histogram(rnd_img)

# Creating and displaying the bar using matplotlib
plt.bar(left=[0, 1, 2, 3], height=hist[0], align="center", width=0.3)
plt.xticks([0, 1, 2, 3], fontsize=20)
plt.yticks(np.arange(0, 15, 2), fontsize=20)
