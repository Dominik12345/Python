# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:40:20 2017

@author: kahl
"""

# IMPORT PACKAGES --->
import json

from filterpy.kalman import KalmanFilter

import matplotlib.pyplot as plt


# <--- IMPORT PACKAGES


# READ DATA FILES --->

file = open("C:/Users/kahl/Documents/Data/review_observation_json.txt",'r')
observation_data =json.loads( file.read() )
file.close()


# <--- READ DATA FILES
