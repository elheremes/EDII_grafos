# import numpy as np
import DLList as dll
import Queue as qu
import Word as wd


class GraphNode:
    def __init__(self, key, data=None):
        self.__key = key
        if data is None:
            self.__data = key
        else:
            self.__data = data
        self.__adj = dll.DLinkedList()
        
    def getVal(self):
        return self.__key

    def getData(self):
        return self.__data

    def setVal(self, val):
        self.__data = val
    
    def getAdj(self):
        return self.__adj


class GraphList:
    def __init__(self, V=0):
        if V < 0:
            V = 0
        self.__V = V
        self.__A = 0
        if V > 0:
            self.__adj = {i: GraphNode(i) for i in range(self.__V)}
        else:
            self.__adj = {}
        # listAux = [GraphNode(i) for i in range(self.__V)]
        # self.__adj = np.array(listAux)
        # seria melhor aqui uma HashTable?

    def insertVer(self, v, value):
        if v in self.__adj:
            self.__adj[v].setVal(value)
        else:
            self.__adj[v] = GraphNode(v, value)
            self.__V += 1
            
    def insertArc(self, v1, v2):
        if self.__adj[v1].getAdj().search(self.__adj[v2]) is None:
            self.__adj[v1].getAdj().insertOrd(self.__adj[v2])
            self.__adj[v2].getAdj().insertOrd(self.__adj[v1])
            self.__A += 1
            # += 2? Não?

    def deleteArc(self, v1, v2):
        if self.__adj[v1].getAdj().searchDelete(
                self.__adj[v2].getVal())is not None:
            self.__adj[v2].getAdj().searchDelete(self.__adj[v1].getVal())
            self.__A -= 1

    def show(self):
        for key in self.__adj:
            strOut = ""
            strOut += "Vértice: " + str(key) + " | Adjacências:"
            aux = self.__adj[key].getAdj().getFirst()
            while aux is not None:
                strOut += " " + str(aux.getVal())
                aux = self.__adj[key].getAdj().getNext()
            print(strOut)
            
    def numberAdj(self):
        return self.__A

    def numberVer(self):
        return self.__V

    # 0 Branco
    # 1 Cinza
    # 2 Preto
    def BFS(self, s):
        color = {}
        dist = {}
        pred = {}
        for key, item in self.__adj.items():
            color[item] = 0
            dist[item] = -1
            pred[item] = None

        if s in self.__adj:
            s = self.__adj[s]
        else:
            return None
        
        color[s] = 1
        dist[s] = 0
        pred[s] = None  # Necessário?
        Q = qu.Queue()
        Q.enqueue(s)
        while Q.size() != 0:
            print(Q)
            u = Q.dequeue()
            ptr = self.__adj[u.getVal()].getAdj().getFirst()
            while ptr is not None:
                if color[ptr] == 0:
                    color[ptr] = 1
                    dist[ptr] = dist[u] + 1
                    pred[ptr] = u
                    Q.enqueue(ptr)
                ptr = self.__adj[u.getVal()].getAdj().getNext()
            color[u] = 2


if __name__ == "__main__":
    g = GraphList()

    dado1 = wd.Word("r")
    dado2 = wd.Word("s")
    dado3 = wd.Word("t")
    dado4 = wd.Word("u")
    dado5 = wd.Word("v")
    dado6 = wd.Word("w")
    dado7 = wd.Word("x")
    dado8 = wd.Word("y")
    
    g.insertVer("r", dado1)
    g.insertVer("s", dado2)
    g.insertVer("t", dado3)
    g.insertVer("u", dado4)
    g.insertVer("v", dado5)
    g.insertVer("w", dado6)
    g.insertVer("x", dado7)
    g.insertVer("y", dado8)
    
    g.insertArc("s", "w")
    g.insertArc("s", "r")
    g.insertArc("r", "v")
    g.insertArc("w", "t")
    g.insertArc("w", "x")
    g.insertArc("t", "u")
    g.insertArc("t", "x")
    g.insertArc("x", "y")
    g.insertArc("x", "u")
    g.insertArc("u", "y")

    g.BFS("s")
    
    g.show()

    
