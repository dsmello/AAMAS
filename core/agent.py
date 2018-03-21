from numpy import random as np_ramdom
import random


class Agent(object):
    links = []
    bias = []
    memory = []

    coin = False
    live = True
    life_time = 0
    rule_to_recive_coin = True

    class Rule:

        pass

    def transfer_coin(self, agent):

        if self.coin:
            agent.accept_coin()
            self.coin = False

    def accept_coin(self):

        if not self.coin:
            self.coin = True

    def core(self):

        security = random.SystemRandom()
        agent = security.choice(self.links)
        self.transfer_coin(agent)

    def check(self):

        return self.coin

    def set_coin(self):
        self.coin = True

    def set_neighbors(self, agent):
        self.links.append(agent)

    def __str__(self):

        if self.coin:
            return "[X]"

        return "[ ]"
