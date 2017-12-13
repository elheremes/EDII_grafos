import numpy as np


class GraphMatrix:
    def __init__(self, V):
        if V <= 0:
            V = 1
        self.__V = V
        self.__A = 0
        self.__adj = np.zeros((V, V))

    def insertArc(self, v1, v2):
        if self.__adj[v1, v2] == 0:
            self.__adj[v1, v2] = 1
            self.__A += 1

    def deleteArc(self, v1, v2):
        if self.__adj[v1, v2] == 1:
            self.__adj[v1, v2] = 0
            self.__A -= 1

    def show(self):
        for i in range(self.__V):
            strOut = ""
            strOut += "Vértice: " + str(i) + " | Adjacências:"
            for j in range(self.__V):
                if self.__adj[i, j] == 1:
                    strOut += " " + str(j)
            print(strOut)

    def numberAdj(self):
        return self.__A

    def numberVer(self):
        return self.__V


if __name__ == "__main__":
    g = GraphMatrix(5)
    g.insertArc(0, 1)
    g.insertArc(0, 2)
    g.insertArc(1, 4)
    g.insertArc(2, 3)

    g.show()
