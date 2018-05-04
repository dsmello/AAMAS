import numpy as np


def findNE(M):
    valor_de_x = float("+inf")
    valor_de_y = float("+inf")
    coluna_atual = 0
    nev = []
    ne = []
    for x, y in M:
        linha_atual = 0
        for valor in x, y:
            if valor[0] * 0.5 <= valor_de_x and valor[1] * 0.5 <= valor_de_y:
                valor_de_x = valor[0]
                valor_de_y = valor[1]
                linha_de_x = linha_atual
                coluna_de_y = coluna_atual
                nev.clear()
                ne.clear()
                ne.append([linha_de_x, coluna_de_y])
                nev.append([valor_de_x, valor_de_y])
            linha_atual += 1
        coluna_atual += 1
    return ne, nev


teste1 = np.array([[-1, -1], [-10, 0]])
teste2 = np.array([[0, -10], [-5, -5]])
ne, nev = findNE([teste1, teste2])

print(ne)
print(nev)
