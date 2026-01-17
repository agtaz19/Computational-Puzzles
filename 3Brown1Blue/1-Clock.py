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
number_of_simulations = 1
hour_total_terminated = [0,0,0,0,0,0,0,0,0,0,0,0] #List number of times it ended on each hour

for i in range(0, number_of_simulations):
    visited_every_hour = False #Flag to check if every hour has been visited
    hour_location = 0 #initial location


    while(not visited_every_hour):
        hour_visted_list = [True, False, False, False, False, False, False, False, False, False, False, False] #list of hours visited
        move_direction = r.random()

        if(move_direction < probability_right):
            hour_location = (hour_location + 1) % 12
        else:
            hour_location = (hour_location - 1) % 12
        
        hour_visted_list[hour_location] = True
        
        if(all(hour_visted_list) == True):
            hour_total_terminated[hour_location] += 1
            visited_every_hour == True

print("Number of simulations: ", number_of_simulations)
print("Hour termination counts: ", hour_total_terminated)
print("Probability of terminating on 6: ", hour_total_terminated[6]/number_of_simulations)
