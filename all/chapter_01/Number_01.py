# Color histogram for a tiny randomly generated image

# import statements
import numpy as np
import matplotlib.pyplot as plt


# Creating a random image and convert it to a 2bit image
rnd_img = np.random.uniform(low=0, high=3, size=(5, 5))
rnd_img = np.unit8(rnd_img)
