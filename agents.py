from mesa import Agent
import math
import random

# sigmoide k = curve coefficient , x = input
sigmoide = lambda k, x: 0.5 + 0.5 * math.tanh(k * x / 2)
justpositives = lambda x: x if x >= 0 else 0


class DefenceAgent(Agent):

    def __init__(self, unique_id, model, function_of_activation=sigmoide):

        super().__init__(unique_id, model)
        self.key = False
        self.number_of_actions = 0

        self.energy = 0
        self.cost_of_energy_to_bird = 500
        self.energy_rate = 5
        self.energy_penality_for_tranfer = 0
        self.energy_limit = 500

        self.neighbors = 0
        self.neighbors_alive = 0

        self.function_of_activation = function_of_activation

        # Receive a tuple (danger (1, 0), size_of_danger (0, 100), key(1, 0), help (1, 0))
        self.mail = []

    def new_agent(self):

        if self.energy >= self.cost_of_energy_to_bird:
            pass

    def message(self) -> tuple:
        pass

    def step(self):
        """ The agent's step will go here. """
        self.energy += self.energy_rate

        if self.energy < 0:
            return

        other_agent = random.choice(self.model.schedule.agents)

        if self.energy >= self.energy_limit:
            other_agent.energy = self.energy_limit

        else:
            other_agent.energy += justpositives(self.energy)

        self.energy = self.energy_penality_for_tranfer

        if self.energy >= self.energy_limit:
            self.energy = self.energy_limit
