import pandas as pd
import csv
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#Read Dataset from file
dataSet=pd.read_csv("dataset.csv")
#Load Data by each column
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
        print("Error in Search:\nNo result match with the dataset \nTry with a valid value which would match with the data set \"" + searchTerm +"\"") #If the searchResults list is empty then an error message is outputted




#####################################################
#
#              Averages
#
#####################################################
def averages():
    print("Welcome")


#####################################################
#
#
########################Calling Menu##############
#
#
#####################################################
menu(gender,educationLevel,institution,itStudent,internetType,networkType,adaptivityLevel)