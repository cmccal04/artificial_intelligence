#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 3.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

from bt.robot_behavior import robot_behavior
from bt.globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH, CHARGING, NUM_CLEANS

# Main body of the assignment
current_blackboard = btl.Blackboard()

#set battery level
battery_ans = int(input("Enter a battery level (int between 0 and 100): "))
current_blackboard.set_in_environment(BATTERY_LEVEL, battery_ans)

#begin in either general cleaning or spot cleaning
state_ans = input("Which mode is the vacuum in? (answer 'Spot' or 'General'): ")
if state_ans == 'Spot':
    current_blackboard.set_in_environment(SPOT_CLEANING, True)
    current_blackboard.set_in_environment(GENERAL_CLEANING, False)
elif state_ans == 'General':
    current_blackboard.set_in_environment(GENERAL_CLEANING, True)
    current_blackboard.set_in_environment(SPOT_CLEANING, False)

    # set num_cleans
    cleans_ans = int(input("How many cleans should occur during general cleaning? "))
    current_blackboard.set_in_environment(NUM_CLEANS, cleans_ans)
else:
    # default general clean mode
    current_blackboard.set_in_environment(GENERAL_CLEANING, True)
    current_blackboard.set_in_environment(SPOT_CLEANING, False)

# set dusty spot
dusty_ans = input("Is there a dusty spot? (enter Y or N): ")
if dusty_ans == 'Y':
    current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, True)
else:
    current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)

#set the rest of the globals
current_blackboard.set_in_environment(HOME_PATH, "")
current_blackboard.set_in_environment(CHARGING, False)

run_times = int(input("Finally, how many times would you like the loop to run? "))

count = 0
done = False
while not done:

    # Each cycle in this while-loop is equivalent to 1 second time

    # if charging is done, make charging false
    if current_blackboard.get_in_environment(BATTERY_LEVEL, 0) == 100:
        current_blackboard.set_in_environment(CHARGING, False)

    # Evaluate the behavior tree
    print('================================' + str(count) + '================================================')
    # notify user of the battery level
    print('Battery Level: ' + str(current_blackboard.get_in_environment(BATTERY_LEVEL, 0)))
    result = robot_behavior.evaluate(current_blackboard)
    print('================================================================================')

    # deplete the battery
    current_blackboard.set_in_environment(BATTERY_LEVEL, 
                                          current_blackboard.get_in_environment(BATTERY_LEVEL, 0) - 1)

    # Step 3: Determine if your solution must terminate
    count += 1
    if count == run_times:
        done = True