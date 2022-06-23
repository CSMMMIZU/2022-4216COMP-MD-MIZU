import pandas as pd
import csv
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
#Read Dataset from file
dataSet=pd.read_csv("dataset.csv")
#Load Data
gender=dataSet["Gender"]
educationLevel=dataSet["Education Level"]
institutionType=dataSet["Institution Type"]
itStudent=dataSet["IT Student"]
internetType=dataSet["Internet Type"]
networkType=dataSet["Network Type"]
adaptivityLevel=dataSet["Adaptivity Level"]
listLi=[]
#################GENDER
totalGirl=0
totalBoy=0
for i, val in gender.iteritems():
     listLi.append(gender[i])
for i in range(0,len(listLi)):
      if "Boy" in listLi[i]:
        totalBoy=totalBoy+1
      elif "Girl" in listLi[i]:
        totalGirl=totalGirl+1
avgBoy=((totalBoy*100))/len(gender)
avgGirl=((totalGirl*100))/len(gender)
print(avgGirl,avgBoy)
############EDULEVEL
totalSchool=0
totalCollege=0
totalUniversity=0
for i, val in educationLevel.iteritems():
     listLi.append(educationLevel[i])
for i in range(0,len(listLi)):           
     if "School" in listLi[i]:
      totalSchool=totalSchool+1
     elif "College" in listLi[i]:
      totalCollege=totalCollege+1
     elif "University" in listLi[i]:
      totalUniversity=totalUniversity+1

avgSchool=(totalSchool*100)/len(educationLevel)
avgCollege=(totalCollege*100)/len(educationLevel)
avgUniversity=(totalUniversity*100)/len(educationLevel)
print(avgCollege,avgSchool,avgUniversity)
#######INSTITUTION TYPE
totalGov=0
totalNonGov=0
for i, val in institutionType.iteritems():
     listLi.append(institutionType[i])
for i in range(0,len(listLi)):
      if"Non Government" in listLi[i]:
        totalNonGov=totalNonGov+1
print(totalGov)
avgNonGov=(totalNonGov*100)/len(institutionType)
avgGov=100-avgNonGov
print("Gov",avgGov,"Non",avgNonGov)
######IT STUDENT
totalIt=0
totalNoIt=0
for i,val in itStudent.iteritems():
  listLi.append(itStudent[i])
for i in range(0,len(listLi)):
  if "Yes" in listLi[i]:
    totalIt=totalIt+1
avgIt=(totalIt*100)/len(itStudent)
avgNoIt=100-avgIt
##############Internet Type
totalWifi=0
for i, val in internetType.iteritems():
     listLi.append(internetType[i])
for i in range(0,len(listLi)):
      if"Wifi" in listLi[i]:
        totalWifi=totalWifi+1
avgWifi=(totalWifi*100)/len(listLi)
avgMobileData=100-avgWifi
###############NETWORK TYPE
total3G=0
for i, val in networkType.iteritems():
  listLi.append(networkType[i])
for i in range (0,len(listLi)):
  if "3G" in listLi[i]:
    total3G=total3G+1
avg3G=(total3G*100)/len(networkType)
avg4G=100-avg3G
###################ADAPTIVITY LEVEL
totalLow=0
totalModerate=0
for i,val in adaptivityLevel.iteritems():
  listLi.append(adaptivityLevel[i])
for i in range(0,len(listLi)):
  if "Low" in listLi[i]:
    totalLow=totalLow+1
  elif "Moderate" in listLi[i]:
    totalModerate=totalModerate+1
avgLow=(totalLow*100)/len(adaptivityLevel)
avgModerate=(totalModerate*100)/len(adaptivityLevel)
avgHigh=100-avgLow-avgModerate
#####################OUTPUT
print(avgIt,avgNoIt,avgGov,avgNonGov,avgBoy,avgGirl,avgCollege,avgUniversity,avgSchool,avgMobileData,avgWifi,avg3G,avg4G,avgHigh,avgLow,avgModerate)
###PIE CHART
print("AVg Boy",avgBoy)
ResultNames=["Boy","Girl"]
ResultValues=np.array[avgBoy,avgGirl]
plt.pie(ResultValues,labels=ResultNames)
plt.show()