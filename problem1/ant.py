import random as rand

class Ant():
    def __init__(self, gridSize) -> None:
        self.gridSize = gridSize
        self.position = [rand.randint(0,self.gridSize-1), rand.randint(0,self.gridSize-1)]
        self.name = "Ant"

    def moveUp(self):
        if self.position[0] > 0: 
            self.position[0] -= 1


    def moveDown(self):
        if self.position[0] < self.gridSize - 1:
            self.position[0] += 1 


    
    def moveLeft(self):
        if self.position[1] > 0:
            self.position[1] -= 1



    def moveRight(self):
        if self.position[1] < self.gridSize - 1:
            self.position[1] += 1


    def moveRandom(self):
        movement = rand.choice(['up', 'down', 'right', 'left'])
        if movement == 'up':
            self.moveUp()
        elif movement == 'down':
            self.moveDown()
        elif movement == 'right':
            self.moveRight()
        else:
            self.moveLeft()
        


ant = Ant(10)