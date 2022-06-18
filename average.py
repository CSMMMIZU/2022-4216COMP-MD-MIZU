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
listLi=[]
myVariable=""
AvgBoy=0
AvgGirl=0
TotalGirl=0
TotalBoy=0
for i, val in gender.iteritems():
     listLi.append(gender[i])
     for i in range(0,len(listLi)):
      if "Boy" in listLi[i]:
        TotalBoy=TotalBoy+1
      elif "Girl" in listLi[i]:
        TotalGirl=TotalGirl+1
AvgBoy=((TotalBoy*100))/len(gender)
AvgGirl=((TotalGirl*100))/len(gender)
print(AvgGirl,AvgBoy)

              
    
