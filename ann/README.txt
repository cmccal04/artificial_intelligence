Artificial Intelligence Assignment 6: Gardens of Heaven

Name: Cullen McCaleb
Date: 12/15

This program, iris_ann.py, trains an artifical neural network to classify 
types of Iris plants, based on Fisher's Iris Database which specifies sepal 
and petal width and length. Additionally, this program classifies the plants 
from user input using the neural network.

Program Details
- Data is cleaned using the steps specifiied in Lecture 21:
        (1) Consolidation and Cleaning
        (2) Selection and Preprocessing
        (3) Transformation and Encoding
- The algorithm used in the artifical neural network is backward propagation.
- Uses activation functions ReLU and Softmax

Assumptions
- The file 'iris_data.txt' has 5 columns representing sepal length, sepal width,
 petal length, and petal widtth, and labels. Also, the file is not missing any 
 values.
- There are only 3 labels.
- A learning rate (0.01), number of epochs (1000), random seed (42), train-test
 split (80/20) are all appropriate values for the task at hand (these values 
 were not chosen for a specific reason, other than that they happened to worked 
 well).
- The user provides valid numerical input.
- There are no errors in loading the file.

Program Usage
- Run the program with the command pythion3 iris_ann.py
- Running the program will show the Mean Absolute Error at each hundred Epoch,
  and print the final test accuracy. It will then ask the user to either exit
  the program, or input new values of an Iris to classify it.

Resources Used
https://builtin.com/machine-learning/relu-activation-function
https://www.geeksforgeeks.org/backpropagation-in-neural-network/
https://www.geeksforgeeks.org/the-role-of-softmax-in-neural-networks-detailed-explanation-and-applications/
