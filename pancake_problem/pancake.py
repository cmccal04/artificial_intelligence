# import heap queue (priority queue) library
import heapq

class Node:
    def __init__(self, state, parent=None, g_cost=0, h_cost=0):
        self.state = state           # The current pancake stack
        self.parent = parent         # The parent node (for path reconstruction)
        self.g_cost = g_cost         # g(n): The cost to reach this node
        self.h_cost = h_cost         # h(n): The heuristic estimate to the goal
    
    def f_cost(self):
        # Returns the total estimated cost (f(n) = g(n) + h(n))
        return self.g_cost + self.h_cost
    
    def __lt__(self, other):
        # used for the priority queue, compares nodes based on f_cost
        return self.f_cost() < other.f_cost()

def heuristic(state, goal_state):
    # Implementation of the gap heuristic function, as specified in the 
    # provided attachement "Landmark Heuristics for the Pancake Problem"
    # Uses the current state and the goal state to calculate this, returns
    # an int.

    gaps = 0
    for i in range(len(state)):
        if state[i] != goal_state[i]:
            gaps += 1
    return gaps


def flip(stack, k):
    # Implementation of the flip action, which flips the top k pancakes 
    # in a given stack. Returns the new stack.

    return stack[:-k] + stack[-k:][::-1]

def is_goal(state, goal):
    # Check if the current state is equal to the goal state. Returns a boolean

    return state == goal

def get_children(node):
    # Create a list of child nodes, which are all the possible flips on a 
    # given parent node's state. Returns the list.

    children = []

    for k in range(2, len(node.state) + 1):
        new_state = flip(node.state, k)
        new_node = Node(new_state, node, node.g_cost + 1, 0)
        children.append(new_node)

    return children

def print_solution(node):
    # Prints every state on the path from the given node to the initial node.
    sol = []
    while node is not None:
        sol.append(node.state)
        node = node.parent
    
    for state in reversed(sol):
        print(state)

def a_star(initial_state, goal_state, heuristic_func):
    # Implementation of the A* algorithm, an informed search algorithm. Uses 
    # an initial state, a goal state, and a heuristic function.

    # initialize the frontier as a heap
    initial_node = Node(initial_state, None, 0, heuristic_func(initial_state, goal_state))
    frontier = []
    heapq.heappush(frontier, initial_node)

    # initialize a set to store the visited nodes
    visited = set()

    # loop through the frontier while it is nonempty
    while frontier:
        # choose a child node from frontier
        current_node = heapq.heappop(frontier)

        # check if the solution has been reached
        if is_goal(current_node.state, goal_state):
            print_solution(current_node)
            return True
        
        visited.add(current_node.state)

        for child in get_children(current_node):
            if child.state not in visited:
                child.h_cost = heuristic_func(child.state, goal_state)
                heapq.heappush(frontier, child)

    # if no solution is found
    return False

def uniform_cost_search(initial_state, goal_state):
    # Implementation of the uniform cost search algorithm. It is the same as 
    # the A* algorithm, except it does not use the heuristic function.

    initial_node = Node(initial_state, None, 0, 0)  # No heuristic for UCS
    frontier = []
    heapq.heappush(frontier, initial_node)
    visited = set()

    while frontier:
        current_node = heapq.heappop(frontier)
        if is_goal(current_node.state, goal_state):
            print_solution(current_node)
            return True
        
        visited.add(current_node.state)

        for child in get_children(current_node):
            if child.state not in visited:
                heapq.heappush(frontier, child)

    return False

def parse_stack_input(input_str):
    # Parse the user input string, input_str, into a tuple of integers 
    # representing the pancake stack.
    # Notes: Used chatGPT as a resource to help write this parse function

    try:
        # Split the input by commas or spaces
        separators = [',', ' ']
        for sep in separators:
            if sep in input_str:
                parts = input_str.strip().split(sep)
                break
        else:
            parts = [input_str.strip()]
        
        # Convert to integers
        stack = tuple(int(part) for part in parts if part != '')
        
        # Check for duplicates
        if len(stack) != len(set(stack)):
            raise ValueError("Duplicate pancake sizes detected.")
        
        return stack
    except ValueError as ve:
        raise ValueError(f"Invalid input: {ve}")

def main():
    # Main function to ask the user for an initial state, and use either 
    # the A* algorithm, or UCS algorithm.

    user_input = input("Enter the stack of pancakes as space-separated or "
                       "comma-separated integers (e.g., 3 6 1 8 2 5 7 4 10 9): ")
    initial_state = parse_stack_input(user_input)
    goal_state = tuple(range(len(initial_state), 0, -1))

    selection = int(input("Select an algorithm option, 1. A* or 2. UCS (type 1 or 2): "))
    if selection == 1:
        if (not a_star(initial_state, goal_state, heuristic)):
            print("A solution could not be found.")
    elif selection == 2:
        if (not uniform_cost_search(initial_state, goal_state)):
            print("A solution could not be found.")

if __name__ == "__main__":
    main()
