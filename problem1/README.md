# Problem 1 QUESTION

With Object Oriented Programming in mind, create the following simulation environment in python:

A 100x100 grid world with 10 randomly placed pieces of food. Note that food cannot share the same coordinate.
An ant class that randomly moves up, down, left, or right at each time step. If an ant tries to step beyond the bounds of the box, it does nothing. Note that food is consumed if an ant shares the same coordinate as the food. Ants can share the same coordinate. Ants starting locations should be random.
Run 1000 simulations with 100 ants, each for 100-time steps. Report the mean and standard deviation of the total food eaten. Feel free to use any Python packages as needed.


# SOLUTION EXPLAINED:

### ant.py file 
- contains the ant class with the movements as functions (up, down, left, right)
- all ants are initialized to have random position assigned upon creation

### world.py file
- contains the class for the grid world
- world is initialized to have ants randomly created/placed  and food randomly created/placed based on given parameters upon creation
- food is set to have unique positions where as ants can share same position
- inherits the Ant class in order to place the ants in the world

### runSimulations.py file
- contains the simulation runs for the problem
- Simulation is set to run 1000 times with 100 ants, 10 pieces of food, and for 100 time steps per simulation
- At the end of each simulation the total food eaten is stored in a list
- At the end of all the simulations the mean and standard deviation for this list is calculated



### To run simulations run python runSimulations.py from .../problem1/ directory



# Some Example Test Run Results for the following inputs
TIME_STEPS = 100
GRID_SIZE = 100
AMOUNT_FOOD = 10
AMOUNT_ANTS = 100
TOTAL_SIMS = 1000

### Run #1
The mean of food eaten across the 1000 simulations is: 3.74
The standard deviation of food eaten across the 1000 simulations is: 1.562817967646904

### Run #2
The mean of food eaten across the 1000 simulations is: 3.792
The standard deviation of food eaten across the 1000 simulations is: 1.5068961477155616

### Run #3
The mean of food eaten across the 1000 simulations is: 3.727
The standard deviation of food eaten across the 1000 simulations is: 1.4981558663904098
