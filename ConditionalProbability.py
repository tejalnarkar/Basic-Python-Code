#Below code randomly creates two vectors
#totals has the number of people in the given age range
#Purchase has the number of people in the age range who have bought the item

from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0
for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = 0.4
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1
        
#P(E|F) in age group 30

PEF = float(purchases[30]) / float(totals[30])
print "P(purchase | 30s): ", PEF
#Output: P(purchase | 30s):  0.398760454901

#P(E) i.e. probability of purchase
PE = float(totalPurchases) / 100000.0
print "P(Purchase):", PE
#Output:P(Purchase): 0.4003
