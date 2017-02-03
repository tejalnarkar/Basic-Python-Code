# Generate dataset

%matplotlib inline
import numpy as np
from pylab import *

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds


scatter(pageSpeeds, purchaseAmount)

# Create training and test set

trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

scatter(trainX, trainY)

# Fit nth  degree polynomial

x = np.array(trainX)
y = np.array(trainY)

p4 = np.poly1d(np.polyfit(x, y, 6))

# Plot polynomial

import matplotlib.pyplot as plt

xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()

from sklearn.metrics import r2_score

r2 = r2_score(testY, p4(testX))

print r2

#OUTPUT when degree is 4: 0.393626926099
#OUTPUT when degree is 6: 0.605011947036
#OUTPUT when degree is 8: 0.300181686124

from sklearn.metrics import r2_score

r2 = r2_score(np.array(trainY), p4(np.array(trainX)))

print r2

#OUTPUT when degree is 4: 0.483122165597
#OUTPUT when degree is 6: 0.602544170711
#OUTPUT when degree is 8: 0.642706951469

# From the above outputs we can infer that the r square for the polynomial with degree 4 is not good for training and testing data both
# The R square is good for the training and testing data for the polynomial with degree 6
# The R square for polynomial with degree 8 is good for training data and not so good for test data





