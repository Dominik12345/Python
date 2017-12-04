# read or generate data

import json

file = open("C:/Users/kahl/Documents/Data/review_observation_json.txt",'r')
observation_data = json.loads( file.read() )
file.close()



x = observation_data['time']
y1 = observation_data['y1']
y2 = observation_data['y2']


# write into json file

with open("data.txt",'w') as outfile:
    json.dump( [x,y1,y2] , outfile )
 
file = open('C:/Users/kahl/Documents/Data/data_pythonplottest.txt', 'w')
file.write( str([x,y1,y2] ) )
file.close()