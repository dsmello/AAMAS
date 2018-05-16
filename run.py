from models import *
from agents import *
import matplotlib.pyplot as plt
import numpy as np

model = PowerGridModel(10, 10)
for i in range(100):
    model.schedule.step()

key = True

agent_counts = np.zeros((model.grid.width, model.grid.height))

for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()
plt.show()

print(agent_counts)
