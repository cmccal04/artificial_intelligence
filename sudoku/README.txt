Artificial Intelligence Assignment 4: Constraint Satisfaction

Name: Cullen McCaleb
Date: 11/12

Goal: Create a python program, sudoku.py, which can solve a given sudoku puzzle
      by framing it as a constrain satisfaction problem.

Board Representation - The board is represented by a 2D list.
Variables - The variables in this problem are the individual cells, of which 
            there are 81.
Domains - The domain for each variable is the set of integers from 1 to 9.
Constraints - The constrains are in accordance with the rules of sudoku: each 
              digit in a single row, column, or box must be unique.
Algorithm - A backtracking algorithm is used

How to run: 
    - Run the program with the command python3 sudoku.py
    - The user will be asked to enter 0 or 1, for the easy or hard board
    - Once a board is selected, it will be printed. Then, the solved board 
      will be printed underneath.

 