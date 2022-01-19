#Fourth B4 file
#Author: Bill Han
#Date: October 2021
#This is my fourth CSV file

import library #This imports the library
import math #This imports the math function

incomeCol = {"income": 29, "country": 0}
hungerCol = {"poverty": 2, "country": 0} #These are the columns for income, country, poverty

incomeInfo = library.loadList("Book1.csv") #Importing the first CSV file
hungerInfo = library.loadList("ghi_data_csv.csv") #Importing the second CSV file
myList = []#Variable name
#The function of this program is to find the correlation between two different files. The closer
#it is to 1, the more correlation that it has. This is called the Pearson Correlation.

def myIsNumeric(num):
	return num.isnumeric and num != '.' 
#The code is messy so this fixes the problem when the value is 0 or someting else that's not a value

def getMean(list): #Command
    sum = 0 #Sum starts at 0
    size = 0 #Size starts at 0
    for i in list:
    	if(myIsNumeric): #Check if data is not empty
        	sum+=int(i)
        	size+=1 #Adds on to the size for averaging
    return sum/size #Returns the average

def getCorr(l1, l2): #Command
    num = 0
    for i in range(0, len(l1)):
        a = float(l1[i])-getMean(l1)
        b = float(l2[i])-getMean(l2) #This is part of the Pearson formula
        num+=a*b #This is part of the numerator
    s1 = 0
    s2 = 0 #These are part of the denominator
    for i in range(0, len(l1)):
        a = float(l1[i])-getMean(l1)
        a = a*a #Multiplies the variables
        s1+=a #This is the first sum
    for i in range(0, len(l2)):
        a = float(l2[i])-getMean(l2)
        a = a*a #Multiplies the variables
        s2+=a #This is the second sum
    s1 = math.sqrt(s1*s2) #Square roots s1 using the math import
    return num/s1

income = incomeInfo[29][incomeCol["income"]] #Defining the location of the average income
hunger = hungerInfo[2][hungerCol ["poverty"]] #Defining the location of the hunger index
fi = [] #This is fixed income
fh = [] #This is fixed hunger
#This is because there are values of 0 and other things (dumb data)

for i in range(0, len(income)):
	if(not myIsNumeric(income[i])):
		fi.append(0) #Clean up data if they are empty
	else:
		fi.append(int(income[i]))

for i in range(0, len(hunger)):
	if(not myIsNumeric(hunger[i])):
		fh.append(0) #Clean up data if they are empty
	else:
		fh.append(int(hunger[i]))

coef = getCorr(fi, fh)
coef = round (coef, 5) #Rounds the final answer to the nearest 5 decimals

print(coef) #Print function

