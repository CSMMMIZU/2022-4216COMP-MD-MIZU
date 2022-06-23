import matplotlib.pyplot as plt
import numpy as np
import math
num1=35
num2=25
num3=25
num4=15
y = np.array([num1, num2, num3, num4])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 
print("num1",num1)