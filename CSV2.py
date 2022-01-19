#Second B4 file
#Author: Bill Han
#Date: October 2021

import library #This imports the library
#This is my second CSV file

#Country,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,
#2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,Info

incomeCol = {"income": 29, "country": 0}
hungerCol = {"poverty": 2, "country": 0}
#These are the columns for income and country and poverty and country respectively

incomeInfo = library.loadList("Book1.csv") #Importing the first CSV file
hungerInfo = library.loadList("ghi_data_csv.csv") #Importing the second CSV file


mylist = []
#Variable name

for i in range(0, len(incomeInfo)):
	income = incomeInfo[i][incomeCol["income"]]
	hunger = hungerInfo[i][hungerCol ["poverty"]]
	hungerCode = incomeInfo[i][incomeCol["country"]]
	#Defining each variable
	if income != '' and hunger!= '':
		ratio = float (income)/ float (hunger)
		#This is the command to find the ratio (We take the income and divide it by the hunger index)
	c = 0
	while c < len (hungerInfo) and hungerInfo[c][hungerCol["country"]].lower() !=hungerCode.lower():
		c += 1
	if c < len(hungerInfo):
		country = hungerInfo[c][hungerCol["country"]]
		#Prints country names that appear in both of the imported CSV files
	else:
		country = "Unknown"
		#Prints out unknown in the list if both files don't both have that same country

	newratio = round (ratio, 1) 
	#This rounds the ratio to the nearest tenth because there would have been 20ish numbers after the decimal

	mylist.append([country, income, hunger, newratio])
	#Puts the strings and integers into a list (The country is a string while the other variables are integers)


#Print Command
for c in mylist:
	print (c)
