# Construct Dataset
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)
money=np.random.normal(3,1,1000)
happiness=np.random.normal(50.0,10.0,1000)/money
plt.scatter(money,happiness)
plt.xlabel('Money')
plt.ylabel('Happiness')
plt.show()

#Construct the polynomial model using polyfit
x=np.array(money)
y=np.array(happiness)
p4=np.poly1d(np.polyfit(x, y, 4))

#Plot the regression-curve along with the scatter plot
xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()

#Get R-square value
from sklearn.metrics import r2_score
r2 = r2_score(y, p4(x))
print r2
#OUTPUT: 0.82937663963
