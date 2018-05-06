import terminal


def model(input_info):
    info = str(input_info)
    info = info.upper()

    if 0 < int(len(info)) > 1:
        raise TypeError("The size of information need to be '1 char'!\n")

    return "[" + info + "]"
