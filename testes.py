import pylab as plt
import numpy as np

X = np.linspace(0,2,1000)
Y = X**2 + np.random.random(X.shape)

plt.ion()
graph = plt.plot(X,Y)[0]

i = 0
i_max = 10000
while i<i_max:
    Y = X**2 + np.random.random(X.shape)
    graph.set_ydata(Y)
    plt.draw()
    plt.pause(0.01)
    i += 1
