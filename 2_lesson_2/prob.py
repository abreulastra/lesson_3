# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:38:49 2016

@author: AbreuLastra_Work
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import collections 
import scipy.stats as stats

#Leson 1_1 Unit 2

mean = 0
variance = 1
sigma = np.sqrt(variance)
x = np.linspace(-3,3,100)
plt.plot(x, mlab.normpdf(x,mean,sigma))

plt.savefig("normal_dist.png")

# Lesson 2_1

testlist = [1, 4, 5, 6, 9, 9 ,9]

#Finding frequencies

c = collections.Counter(testlist)
print(c)

count_sum = sum(c.values())

for k, v in c.iteritems():
    print("The frecuency of number" + str(k) + " is " + str(float(v) / count_sum))

# Creating a bloxplot

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.savefig("boxplot.png")

# Creating a histogram
plt.hist(x, histtype='bar')
plt.savefig("his.png")


# QQplot
plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show()
plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist='norm', plot=plt)
plt.show()

plt.figure()
graph_qq = stats.probplot(x, dist="norm", plot=plt)
plt.show()
plt.savefig("qq_plot.png")