def _bigger(x, y):
    # Retorna o indice do maior valor entre "x" e "y"

    return 0 if x > y else 1


def _vote(x, y, database):
    # Manipila a database, incerindo o voto

    y *= 2
    database[x + y] += 1


def findNE(M):
    # A entrada de M deve ser uma lista ou tupula
    # Ex.: [[[a, b], [c, d]],
    #       [[e, f], [g, h]]]
    # Onde teremos M[x][y][z]
    # x = linha     y = coluna      z = elemento (Player 1, ou 2)
    #
    # Em python se começa contar o 0.

    # possiveis jogadas em uma matrix 2x2

    jogada = {0: [0, 0], 1: [0, 1], 2: [1, 0], 3: [1, 1]}

    # votos em cada possivel jogada

    votos = [0, 0, 0, 0]

    p1_1 = _bigger(M[0][0][0], M[1][0][0])
    p1_2 = _bigger(M[0][1][0], M[1][1][0])
    _vote(p1_1, 0, votos)
    _vote(p1_2, 1, votos)

    p2_1 = _bigger(M[0][0][1], M[0][1][1])
    p2_2 = _bigger(M[1][0][1], M[1][1][1])
    _vote(0, p2_1, votos)
    _vote(1, p2_2, votos)

    # Jogada decidida

    ne = jogada[votos.index(max(votos))]

    x = ne[0]
    y = ne[1]

    # valor da jogada decidida

    nev = M[x][y]

    return ne, nev


def findmixedNE(M):
    # Variables :

    a = M[0][0][0]
    b = M[0][0][1]
    c = M[0][1][0]
    d = M[0][1][1]
    e = M[1][0][0]
    f = M[1][0][1]
    g = M[1][1][0]
    h = M[1][1][1]

    # Basic expression's variables

    sigma_up = (h - f) / (b + h - f - d)
    sigma_down = 1 - sigma_up

    sigma_left = (g - h) / (a + g - c - e)
    sigma_right = 1 - sigma_left

    payoff_probability = [[sigma_up * sigma_left, sigma_up * sigma_right],
                          [sigma_down * sigma_left, sigma_down * sigma_right]]

    sigmas = [[sigma_up, sigma_down], [sigma_left, sigma_right]]

    # Output's

    pp = payoff_probability
    payoff = [[[pp[0][0] * a, pp[0][0] * b], [pp[0][1] * c, pp[0][1] * d]],
              [[pp[1][0] * e, pp[1][0] * f], [pp[1][1] * g, pp[1][1] * h]]]

    ne = sigmas
    nev = payoff

    return ne, nev
