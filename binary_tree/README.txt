Artificial Intelligence Assignment 1: Behavior Trees

Name: Cullen McCaleb
Date: 10/04
LATE TOKEN USED, new due date Friday 10/04

- This program simulates a vacuum robot by using a behavior tree.
- The framework of my solution was provided.

Files I implemented:
    sequence.py - implements the squence composite
    dusty_spot.py - implements the dusty spot condition
    general_cleaning.py - implements the general cleaning condition
    spot_cleaning.py - implements the spot cleaning condition
    until_fail.py - implements the until fail decorator
    always_fail.py - implements the always fail task
    charge.py - implements the charge fail task
    clean_floor.py - implements the clean floor task
    clean_spot.py - implements the clean spot task
    do_nothing.py - implements the do nothing task
    done_general.py - implements the done general task
    done_spot.py - implements the done spot task
    go_home.py - implements the go home task

Files I updated:
    robot_behavior.py - I used the given examples to create a tree based on 
                        the assignment.
    globals.py - Created a new global, NUM_CLEANS, which keeps track of the 
                 amount of times the clean floor task should run before it fails.
    __init__.py - I initialized every new task/condition/composite/decorater.
    main.py - I update the main file to carry out my implementation of the 
              behavior tree.

Overview:
    The program begins by asking the user to set the global variables, including 
    the battery level, cleaning mode, number of cleans, and if there is a dusty spot.
    The program then asks the user how many times the main loop should be run.
    The main loop of the program begins with a notification of the battery level, 
    then prints the state of the nodes while running the tree, and finally reduces
    the battery level by 1.

HOW TO RUN: 
    run the command 'python3 main.py' in terminal. Do not misspell the inputs 
    as there is no error handling.

