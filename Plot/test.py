import json
import plot_function
import numpy as np



# get data from json file
file = open("C:/Users/kahl/Documents/Data/data_pythonplottest.txt",'r')
data = json.loads( file.read() )
file.close()

plot_function.plot2d(data)
