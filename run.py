from models import *
from agents import *
import matplotlib.pyplot as plt
import numpy as np


model = PowerGridModel(10, 10)
for i in range(100):
    model.schedule.step()

print(model.schedule.agents[1].pos)

key = True

agent_counts = np.zeros((model.grid.width, model.grid.height))

for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = list(cell_content)[0].energy
    agent_counts[x, y] = agent_count
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()
plt.show()

print(sum(sum(agent_counts)))
