from world import World
import numpy as np

TIME_STEPS = 100
GRID_SIZE = 100
AMOUNT_FOOD = 10
AMOUNT_ANTS = 100
TOTAL_SIMS = 1000

def testSimulation():
    foodEaten = np.zeros(TOTAL_SIMS)
    for sim in range(TOTAL_SIMS):
        #Reset the world for every simulation
        world = World(GRID_SIZE, AMOUNT_ANTS, AMOUNT_FOOD)
        #perform all the time steps
        for timeStep in range(TIME_STEPS):
            #For each time step check all ant coordinates to see if they match with any food coordinates
            #after check then update the ants position
            for ant in world.ants:
                #check if ant is at food coordinate, if so remove food
                if world.grid[ant.position[0]][ant.position[1]] == 1:
                    world.grid[ant.position[0]][ant.position[1]] = 0
                    #increment the foodEaten count for this simulation
                    foodEaten[sim] += 1
                #update each ants position regardless
                ant.moveRandom()

        #print(f"The world has a total of {world.checkFood()} food pieces left for simulation #{sim + 1}")
    print(f"The mean of food eaten across the {TOTAL_SIMS} simulations is: {np.mean(foodEaten)}")
    print(f"The standard deviation of food eaten across the {TOTAL_SIMS} simulations is: {np.std(foodEaten)}")

testSimulation()