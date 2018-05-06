from agents.abstracts import Agent, State


class AgentOfDefense(Agent):

    def __init__(self):
        print("I'm Defender!!!")

    def __change_state(self, state):
        pass

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
