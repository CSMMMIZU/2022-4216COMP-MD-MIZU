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
internetType=dataSet["Internet Type"]
networkType=dataSet["Network Type"]
adaptivityLevel=dataSet["Adaptivity Level"]
#Menu#
##
###
####
def menu(gender,educationLevel,institution,itStudent,internetType,networkType,adaptivityLevel):
    repeat=True
    selectMenu=input()
    if selectMenu=="1":
        keywordSearch()
    elif selectMenu=="2":
        averages()
    else:
        print("Wrong input!Try Again?")
#####################################################
#
#                 Keyword Search
#
#####################################################
def keywordSearch():
    print("Keyword Search")
    data=[]
    searchResults=[]
    with open("dataset.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:#Reads each row of the CSV file
            data.append(row)
    searchTerm=input() 
    print(len(data))
    for i in range(0,(len(row))):#Used to only search the columns that contain searchable data.
        column = [x[i] for x in data]
        if searchTerm in column:
            for x in range(0,len(data)):
                if searchTerm == data[x][i]:#This compares the input to the individual value of each "cell" in the CSV file in the data List
                    searchResults.append(data[x])
                    print(searchResults)#Outputs the collected rows that contain the search term.
                    print(len(searchResults))

    if len(searchResults) == 0:
        print("Error:\nNo results match \nTry with a valid value \"" + searchTerm +"\"") #If the searchResults list is empty then an error message is outputted




#####################################################
#
#              Averages
#
#####################################################
def averages():

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
    print(avgIt,avgNoIt,avgBoy,avgGirl,avgCollege,avgUniversity,avgSchool,avgMobileData,avgWifi,avg3G,avg4G,avgHigh,avgLow,avgModerate)
###PIE CHART
    print("AVg Boy")
    GenderNames=["Boy","Girl"]
    GenderValues=np.array([avgBoy,avgGirl])
    EduNames=["School","College","University"]
    EduValues=np.array([avgSchool,avgCollege,avgUniversity])
    InstitutionNames=["Government","Non Government"]
    InstitutionValues=np.array([avgGov,avgNonGov])
    ItStatus=["Yes","No"]
    ItValues=np.array([avgIt,avgNoIt])
    InternetNames=["Mobile Data","Wifi"]
    InternetValues=np.array([avgMobileData,avgWifi])
    NetworkNames=["3G","4G"]
    NetworkValues=np.array([avg3G,avg4G])
    adapLvlnames=["High","Moderate","Low"]
    adapValues=np.array([avgHigh,avgModerate,avgLow])
#plt.pie(ResultValues,labels=ResultNames)
#plt.show()
    fig,axs=plt.subplots(2,4)
    axs[0][0].set_title("GENDER")
    axs[0][0].pie(GenderValues,labels=GenderNames)
    axs[0][1].set_title("EDUCATION LEVEL")
    axs[0][1].pie(EduValues,labels=EduNames)
    axs[0][2].set_title("INSTITUTION LEVEL")
    axs[0][2].pie(InstitutionValues,labels=InstitutionNames)
    axs[0][3].set_title("IT STUDENT")
    axs[0][3].pie(ItValues,labels=ItStatus)
    axs[1][0].set_title("INTERNET TYPE")
    axs[1][0].pie(InternetValues,labels=InternetNames)
    axs[1][1].set_title("NETWORK TYPE")
    axs[1][1].pie(NetworkValues,labels=NetworkNames)
    axs[1][2].set_title("ADAPTIVITY LEVEL")
    axs[1][2].pie(adapValues,labels=adapLvlnames)
    axs[1][3].set_visible(False)
    plt.show()

    
    



#####################################################
#
#
########################Calling Menu##############
#
#
#####################################################
menu(gender,educationLevel,institution,itStudent,internetType,networkType,adaptivityLevel)