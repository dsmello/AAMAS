from .agent import Agent
import numpy as np
import random


class Factory(object):
    agents = []
    sinapsis: np.array
    size: int

    class Network:

        def network_plan_standart(self, size):
            return np.random.randint(size, size=(size, size))

    class Start:

        # For a custom start
        pass

    def __init__(self, number_of_agents: int):

        self.size = number_of_agents

        for sample in range(number_of_agents):
            self.agents.append(Agent())

        self.choose_one()
        self.sinapsis = self.Network().network_plan_standart(number_of_agents)

        self.made_sinapsis()

    def choose_one(self):

        sample: Agent

        security = random.SystemRandom()
        sample = security.choice(self.agents)
        sample.set_coin()

    def made_sinapsis(self):

        for agent in self.agents:

            for line in self.sinapsis:

                for number in line:
                    agent.set_neighbors(self.agents[number])

    def get_agents(self):

        return self.agents
