from agents.abstracts import Agent, State


class AgentOfAttack(Agent):

    def __init__(self):
        print("I'm Attacker!!!")

    def __change_state(self, state):
        pass

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

        pass

    def send_msg(self, agent):
        # Send msg, whit data to another agent.

        pass

    def do(self):
        # Is the principal method of the agent, because, the interpret the agent variables, and :
        # decide the state, what msg send's, read mail, made actions.
        # The method 'do', pass to state him self, and the state, using the parameters of the agent chose the action.
        # Ex.: self.state.do(self)

        self.state.do(self)
