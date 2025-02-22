Artificial Intelligence Assignment 2: Informed Search

Name: Cullen McCaleb
Date: 10/13
LATE TOKEN USED, new due date Sunday 10/13

1. Five components must be explained to define the Pancake Problem as a searching problem.
    - The initial state is a scrambled stack of 10 pancakes in any order. 
        For example, [5, 8, 10, 1, 3, 4, 7, 9, 2, 6], where 10 is the largest 
        pancake and 1 is the smallest.
    - There is one action available, the flip action. This action means all 
        the pancakes above a given position k are “flipped” at once (their 
        position is reversed). For example, the result of a flip on the example
        initial state above, if k=6, results in the new stack 
        [5, 8, 10, 1, 3, 4, 6, 2, 9, 7].
    - The transition model for the flip action is that the elements from 
        index k to index 10 are reversed.
    - The goal state of the pancake problem is a stack with the largest pancake
        on the bottom, and the smallest on top. For example, 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
    - The path cost for each individual flip is 1.

2. A possible backwards cost function is g(n), where g(n) = the number of total 
    flips to reach state n.

3. A possible heuristic function, h(n), could be the gap heuristic that is
    defined in the attachement "Landmark Heuristics for the Pancake Problem". The
    gap hueristic is essentially the number of stack positions for which the
    pancake at that position is not of adjacent size to the pancak below.

4. and 5. are implemented in the file pancake.py


pancake.py Notes:

    - Run the file using the command python3 pancake.py
    - The program asks for an initial stack. It expects this input to be only
        integers, separated by either spaces or commas.
    - The program then asks which algorithm it should use, and ONLY accepts 
        inputs 1 and 2.
    - Uses the heapq library as the priority queue.
    - My implmentation does not have a specific backwards cost function 
        defined, as it is represented by the g_cost variable for each node.
