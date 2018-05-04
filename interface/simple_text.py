def show_ans(agents):
    print("\n The X mark the spot,\n")

    ans = ''
    count = 1

    for agent in agents:

        if count % 15 == 0:
            ans += "\n"
        ans += str(agent)
        count += 1

    print(ans)
    print("\n")


def get_input(size):
    ans = input("chose a the agent, writing a number.")
    ans = int(ans)
    return ans
