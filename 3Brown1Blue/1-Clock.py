"""
Docstring for 3Brown1Blue.1-Clock
The problem: 
You have a bug on the 12 of the clock with equal probabilty of moving to the left or right hour. What is the probability that 6 is the last hour visited?
"""

#imports
import random as r

#Parameters
probability_right = 0.5
probability_left = 1-probability_right
number_of_simulations = 10

for i in range(0, number_of_simulations):
    visited_every_hour = False #Flag to check if 6 was the last hour visited

    print("Simulation number: " + str(i+1))
    while(not visited_every_hour):
        hour_visted_list = [True, False, False, False, False, False, False, False, False, False, False, False] #list of hours visited
        hour_location = 0 #initial location
        move_direction = r.random()

        if(move_direction < probability_right):
            hour_location = (hour_location + 1) % 12
            print(hour_location)
        else:
            hour_location = (hour_location - 1) % 12
            print(hour_location)
        
        hour_visted_list[hour_location] = True
        
        if(all(hour_visted_list) == True):
            visited_every_hour == True
