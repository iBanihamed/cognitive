import random as rand
from ant import Ant

class World(Ant):
    def __init__(self, gridSize, amountAnts, amountFood) -> None:
        self.gridSize = gridSize
        self.amountAnts = amountAnts
        self.amountFood = amountFood
        self.ants = []
        self.grid = [[0 for x in range(self.gridSize)] for y in range(self.gridSize)]
        self.placeFood()
        self.placeAnts()
    
    def placeFood(self):
        foodPlaced = 0
        while foodPlaced < self.amountFood:
            randomCoordinates = [rand.randint(0,self.gridSize - 1), rand.randint(0, self.gridSize-1)]
            #Ensure that food does not share the same coordinates
            if not self.grid[randomCoordinates[0]][randomCoordinates[1]]:
                self.grid[randomCoordinates[0]][randomCoordinates[1]] = 1
                foodPlaced += 1
               
    def placeAnts(self):
        self.ants = []
        for i in range(self.amountAnts):
            self.ants.append(Ant(self.gridSize))


    def checkFood(self):
        foodLeft = 0
        for row in self.grid:
            foodLeft += row.count(1)
        self.foodAmount = foodLeft
        return self.foodAmount

    def printWorld(self):
        for row in self.grid:
            print(row)

