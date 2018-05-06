from interface.model import model
from agents.abstracts import Agent


class State(object):
    letter = None
    Meaning = None

    def __init__(self):
        raise NotImplementedError("subclasses must override __init__ method!\nYou can't instantiate this class!\n")

    def get_info(self):
        # return info about the state to use on terminal package.

        raise NotImplementedError("subclasses must override get_info method!\n")

    def get_string_info(self):
        # This method implement's the output of the agent state.
        # Using the method model to had a eas pattern of string, receive '1 char' to represent the state

        raise NotImplementedError("subclasses must override string_info method!\n")

    def legend(self):
        # This method return (letter, meaning), info about what letter and your about meaning this state.
        # letter and meaning is string.
        # And if the letter is not be unique, the will raise a Error.

        raise NotImplementedError("subclasses must override legend method!\n")

    def do(self, agent: Agent):
        # this method, receive an agent, interpreter his values and made all necessaries actions.

        raise NotImplementedError("subclasses must override legend method!\n")
