#Third B4 file
#Author: Bill Han
#Date: October 2021

import library #This imports the library
#This is my third CSV file

#Country,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,
#2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,Info

hungerCol = {"poverty": 2, "country": 0}
economicCol = {"ecofreedom": 3, "country": 2}
#These are the columns for income, country, poverty, and economic freedom

hungerInfo = library.loadList("ghi_data_csv.csv") #Importing the second CSV file
economicInfo = library.loadList("efw_cc.csv") #Importing the third CSV file


myList = []
#Variable name


for i in range(1, len(incomeInfo)):
	income = incomeInfo[i][incomeCol["income"]]
	hunger = hungerInfo[i][hungerCol ["poverty"]]
	economic = economicInfo[i][economicCol ["ecofreedom"]]
	hungerCode = incomeInfo[i][incomeCol["country"]]
	country = incomeInfo[i][incomeCol["country"]]
	#Defining each variable
	if income != '' and hunger!= '':
		ratio = float (income)/ float (hunger)
		#This is the command to find the ratio (We take the income and divide it by the hunger index)


	newratio = float (ratio) / float (economicCol['ecofreedom'])
	#Gives first divident

	newnewratio = round (newratio, 1) 
	#Rounds the second value

	myList.append([country, newnewratio]) #Prints out the list

for c in myList:
	print (c)

#Print Command

