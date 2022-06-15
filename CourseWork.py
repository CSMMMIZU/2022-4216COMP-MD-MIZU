import pandas as pd
import csv
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#Read Dataset from file
dataSet=pd.read_csv("dataset.csv")
#Load Data
gender=dataSet["Gender"]
educationLevel=dataSet["Education Level"]
institution=dataSet["Institution Type"]
itStudent=dataSet["IT Student"]
loadShedding=dataSet["Load-shedding"]
internetType=dataSet["Internet Type"]
networkType=dataSet["Network Type"]
device=dataSet["Device"]
adaptivityLevel=dataSet["Adaptivity Level"]
print(len(gender))
print(educationLevel[6])
for i in range(len(gender)):
    print(gender[i])
