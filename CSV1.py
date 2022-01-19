#First B4 file
#Author: Bill Han
#Date: October 2021

import library #This imports the library
#This is my second CSV file

#The original CSV file prints the country name, the year that the information was recorded, hunger index, and hunger severity

hungerData = library.loadList("ghi_data_csv.csv") #Importing the data file

lowHunger = []
moderateHunger = []
seriousHunger = []
#These are the variable names

def sortKey(e):
	return e[0]

hungerData.sort(key=sortKey)

#This sorts all of the countries by their name alphabetically 

for n in range (0, len(hungerData)):

	year = hungerData[n][1]

	year = float(year)

	hungerState = hungerData [n][3]

	if year >= 2016 and hungerState == 'Low':
		lowHunger.append(hungerData[n][0])

	elif year >= 2016 and hungerState == 'Moderate':
		moderateHunger.append(hungerData[n][0])

	elif year >= 2016 and hungerState == 'Serious':
		seriousHunger.append(hungerData[n][0])


	#Eliminated all countries that had their index recorded before 2015

	#Had all three requirements satisfied with Boolean operators

#Print Commands

print(lowHunger)

print(moderateHunger)

print(seriousHunger)