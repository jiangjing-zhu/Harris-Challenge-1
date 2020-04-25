# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
"pip install json"
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('/Users/apple/Documents/GitHub/Harris-Challenge-1/divvy_stations.txt').read())
df=divvy_stations

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system
l1=['num_docks_available']
l2=['num_bikes_available']
A=len(df)
totalnum_docks_available=[(k, sum([x[k] for x in df])) for k in l1][-1][-1]
totalnum_bikes_available=[(k, sum([x[k] for x in df])) for k in l2][-1][-1]
print('average number of empty docks is',totalnum_docks_available/A)
print('average number of bikes at all station in this system is',totalnum_bikes_available/A)
#average number of empty docks is 9.532773109243697
#average number of bikes at all station in this system is 7.7596638655462185      


# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)
l3=['num_bikes_disabled']
totalnum_bikes_disabled=[(k, sum([x[k] for x in df])) for k in l3][-1][-1]
#total bikes in the system=num_bikes_disabled+num_bikes_available+num_docks_available
totalbikes=totalnum_bikes_disabled+totalnum_docks_available+totalnum_bikes_available
print("ratio of bikes that are currently rented to total bikes in the system is",totalnum_docks_available/totalbikes)
#ratio of bikes that are currently rented to total bikes in the system is 0.5502522312766783



# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%
percent_bikes_list=[]
for data in divvy_stations:
    data["percent_bikes_remaining"]="%.2f%%"%((float(data["num_bikes_available"]) / 
                                                     (float(data["num_bikes_disabled"]) +
                                                      float(data["num_docks_available"]) +
                                                      float(data["num_bikes_available"])))*100)

percent_bikes_list.append(data)
print(percent_bikes_list)





