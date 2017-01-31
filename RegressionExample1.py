#Create two variable with normally distributed data
import numpy as np
import matplotlib.pyplot as plt

money=np.random.normal(3,1,1000)
happiness=1+(money+np.random.normal(0,0.1,1000))*3
plt.scatter(money,happiness)
plt.xlabel('Money')
plt.ylabel('Happiness')
plt.show()

#Print value of R square
print (r_value ** 2)
#Output:0.990375002434

#Printing the regression line
def predict(x):
  return slope*x+intercept

line=predict(money)
plt.scatter(money,happiness)
plt.plot(money, line, c='r')
plt.show()
