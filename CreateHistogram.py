# This Statement Generates random numbers that are normally distributed
# The values passed in the normal function are location, scale and size respectively

import numpy as np
x=np.random.normal(200,150,1000)

# Plotting the histogram
%matplotlib inline
import matplotlib.pyplot as plt
plt.hist(x,50)
plt.show()

