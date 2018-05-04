from agents.states.state import State

"""
Is basic reference of agent
"""


class Agent(object):
    state = None

    def __init__(self):

        raise NotImplementedError("subclasses must override __init__ method!\nYou can't instantiate this class!\n")

    def change_state(self):
        # Responsible to change the agent state.

        raise NotImplementedError("subclasses must override change_state method!\n")

    def __valid_state(self):
        # check integrity of agent state, when is crate

        if not self.state:
            raise TypeError("The agent had have a valid state!\n")

        if isinstance(self.state, State):
            raise TypeError("The state of this agent not is instance of ' State class '!\n")

    def __str__(self):
        # Return a basic str info about the agent.

        return self.state.get_string_info()

    def get_info(self):

        return self.state.get_info()

    # check integrity of agent, when is crate
