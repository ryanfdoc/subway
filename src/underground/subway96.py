# Python Script to Print Next Trains Stopping at 96th Street

import os
import requests
import time
import datetime
import underground

from underground import metadata, SubwayFeed

# Grab API Key from Env file
# API_KEY = os.getenv('MTA_API_KEY')

print("WAR DAMN EAGLE")

# Define Train Routes
# Request feeds from 123456S MTA Feed, hardcoded APIkey
ROUTE1 = '1'
ROUTE2 = '2'
ROUTE3 = '3'
feed1 = SubwayFeed.get(ROUTE1,api_key='pRNmvpGMmR9lFcp82OIty307RJzAUkFn4seMMYHe')
feed2 = SubwayFeed.get(ROUTE2,api_key='pRNmvpGMmR9lFcp82OIty307RJzAUkFn4seMMYHe')
feed3 = SubwayFeed.get(ROUTE3,api_key='pRNmvpGMmR9lFcp82OIty307RJzAUkFn4seMMYHe')

# Feed_96th_Train is a dictionary
Feed_96th_Train1 = feed1.extract_stop_dict()
Feed_96th_Train2 = feed2.extract_stop_dict()
Feed_96th_Train3 = feed3.extract_stop_dict()

# Define the next two trains on each line
OneTrainA   = Feed_96th_Train1['1']['120S'][0]
OneTrainB   = Feed_96th_Train1['1']['120S'][1]
TwoTrainA   = Feed_96th_Train2['2']['120S'][0]
TwoTrainB   = Feed_96th_Train2['2']['120S'][1]
ThreeTrainA = Feed_96th_Train3['3']['120S'][0]
ThreeTrainB = Feed_96th_Train3['3']['120S'][1]

# Collect next 2 trains for each train line into a list
Next_Trains = [OneTrainA, OneTrainB, TwoTrainA, TwoTrainB, ThreeTrainA, ThreeTrainB]
# Sort trains by arrival times
Next_Trains.sort()

# define next downtown trains
#nearest_local_time = time.strftime("%I:%M %p",OneTrainA)
#nearest_express_time = time.strftime("%I:%M %p",TwoTrainA)

# calculate time until arrival
current_time = time.strftime("%I:%M %p")

print(current_time)
print(OneTrainA)

#time_until_local = int(((nearest_local_time - current_time) / 60))
#time_until_express = int(((nearest_express_time - current_time) / 60))


# print("1 South Ferry   ",nearest_local_time)
# print("2 South Ferry   ",nearest_express_time)




#Print current time
#print("It's currently  ",time.strftime("%I:%M %p"))

# Print the next two of each train times going downtown
# print("1 South Ferry   ",Feed_96th_Train1['1']['120S'][0])
# print("1 South Ferry   ",Feed_96th_Train1['1']['120S'][1])
# print("2 South Ferry   ",Feed_96th_Train2['2']['120S'][0])
# print("2 South Ferry   ",Feed_96th_Train2['2']['120S'][1])
# print("3 South Ferry   ",Feed_96th_Train3['3']['120S'][0])
# print("3 South Ferry   ",Feed_96th_Train3['3']['120S'][1])

#End of script
