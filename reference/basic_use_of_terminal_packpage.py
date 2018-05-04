from terminal import Command, red, blue, white_bg

program = Command('foo', version='1.0.0')


@program.action
def show(color=True):
    """
    show something.

    :param color: disable or enable colors
    """

    r = red('|show|' * 10)

    # if color:
    #     print(r, blue("america"))
    # else:
    #     print(blue('|show|'*10))

    return r


text = []
times = 5

for n in range(times):
    print(show())
