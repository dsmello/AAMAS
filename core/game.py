from .factory import Factory


def run(size):
    agents = Factory(size).get_agents()

    ans = ''

    for agent in agents:
        ans += str(agent)

    print(ans)
