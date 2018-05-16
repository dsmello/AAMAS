from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from agents import *


class PowerGridModel(Model):
    """A model with some number of agents."""

    def __init__(self, width: int, height: int):

        n = width * height
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, height, False)

        places = []
        for x in range(width):
            for y in range(height):
                places.append((x, y))

        for i in range(n):
            a = DefenceAgent(i, self)
            self.schedule.add(a)

            # Add the agent to grid cell
            self.grid.place_agent(a, places[i])

    def step(self):
        self.schedule.step()
