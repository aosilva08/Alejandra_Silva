# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:59:15 2024

@author: aosilva08
"""
#1. Create an Agent class
#2. Create a World class
#3. Initialize the world
#4. Create a loop
#Ask each agent in sequence to find an empty patch
#Move the agent to the empty patch
#5. End
#Keep it simple (small grid, small number of agents, small number of loops), and utilize the code from the more complex example given in lecture. 

from numpy import random

class Agent:
    def __init__(self, world):
        self.world = world
        self.x, self.y = self.find_empty_patch()
        self.world.grid[self.x][self.y] = 'A'

    def find_empty_patch(self):
        empty_patches = [(x, y) for x in range(self.world.size) for y in range(self.world.size) if self.world.grid[x][y] is None]
        return random.choice(empty_patches)

    def move(self):
        self.world.grid[self.x][self.y] = None
        self.x, self.y = self.find_empty_patch()
        self.world.grid[self.x][self.y] = 'A'

class World:
    def __init__(self, size, num_agents, steps):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = [Agent(self) for _ in range(num_agents)]
        self.steps = steps

    def step(self):
        for agent in self.agents:
            agent.move()

    def display(self):
        for row in self.grid:
            print(' '.join(['.' if cell is None else cell for cell in row]))
        print()

    def run(self):
        for step in range(self.steps):
            print(f"Step {step + 1}")
            self.step()
            self.display()

def main():
    world = World(size=3, num_agents=2, steps=3)
    world.run()

if __name__ == "__main__":
    main()
