from .states.state import State

"""
Is basic reference of agent.
"""


class Agent(object):

    state = None
    mail = None  # We use mail, to easily synchronize the agents per turn.
    neighbors = None  # The another agent's of this agent can communicate.

    def __init__(self):
        # check integrity of agent, when is crate

        raise NotImplementedError("subclasses must override __init__ method!\nYou can't instantiate this class!\n")

    def __change_state(self, state):
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

    def recive_msg(self, data):
        # Recive msg, and do what's necessary, whit the data input and put things on mail.

        raise NotImplementedError("subclasses must override recive_msg method!\n")

    def send_msg(self, agent):
        # Send msg, whit data to another agent.

        raise NotImplementedError("subclasses must override send_msg method!\n")

    def do(self):
        # Is the principal method of the agent, because, the interpret the agent variables, and :
        # decide the state, what msg send's, read mail, made actions.
        # The method 'do', pass to state him self, and the state, using the parameters of the agent chose the action.
        # Ex.: self.state.do(self)

        self.state.do(self)
