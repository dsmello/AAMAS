from builtins import object

from .factory import Factory
from interface import simple_text as ST


class Game(object):
    debug: bool
    agents: list

    def __init__(self, size, debug=False):

        self.agents = Factory(size).get_agents()
        self.debug = debug

    def play(self):

        number = ST.get_input(self.agents.__len__())

        if self.agents[number].check():
            # retorna True, caso ache a moeda
            print("You WIN!!!")
            ST.show_ans(self.agents)
            return True

        print("Try again!")

        if self.debug:
            ST.show_ans(self.agents)

        for agent in self.agents:
            if agent.core():
                break
        return False
