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
number_of_simulations = 1000000
hour_total_terminated = [0,0,0,0,0,0,0,0,0,0,0,0] #List number of times it ended on each hour

for i in range(0, number_of_simulations):
    visited_every_hour = False #Flag to check if every hour has been visited
    hour_location = 0 #initial location
    hour_visted_list = [True, False, False, False, False, False, False, False, False, False, False, False] #list of hours visited

    print("Simulation number: ", i+1)
    while(not visited_every_hour):

        move_direction = r.random()

        if(move_direction < probability_right):
            hour_location = (hour_location + 1) % 12
        else:
            hour_location = (hour_location - 1) % 12
        
        hour_visted_list[hour_location] = True
        
        if(len(set(hour_visted_list)) == 1):
            hour_total_terminated[hour_location] += 1
            visited_every_hour = True
        

print("Number of simulations: ", number_of_simulations)
for i in range(len(hour_total_terminated)): 
    print("Number of termininations on hour ", i, ": ", "{:,}".format(hour_total_terminated[i]))
    hour_total_terminated[i] = hour_total_terminated[i]/number_of_simulations
    print("Percentage of terminations on hour ", i, ": ", "{:.4f}%".format(hour_total_terminated[i]*100))
