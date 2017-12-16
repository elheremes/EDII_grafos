import numpy as np
import DLList as dll
import Word as wd


class GraphNode:
    def __init__(self, key, data=None):
        self.__key = key
        if data is None:
            self.__data = key
        else:
            self.__data = data
        self.__adj = dll.DLinkedList()
        
    def getKey(self):
        return self.__key

    def getVal(self):
        return self.__data

    def setVal(self, val):
        self.__data = val
    
    def getAdj(self):
        return self.__adj


class GraphList:
    def __init__(self, V):
        if V <= 0:
            V = 1
        self.__V = V
        self.__A = 0
        listAux = [GraphNode(i) for i in range(self.__V)]
        self.__adj = np.array(listAux)
        
    def changeVerValue(self, v, value):
        if v <= self.__V:
            self.__adj[v].setVal(value)
        
    def insertArc(self, v1, v2):
        if self.__adj[v1].getAdj().search(self.__adj[v2]) is None:
            self.__adj[v1].getAdj().insertOrd(self.__adj[v2])
            self.__adj[v2].getAdj().insertOrd(self.__adj[v1])
            self.__A += 1
            # += 2? Não?

    def deleteArc(self, v1, v2):
        if self.__adj[v1].getAdj().searchDelete(self.__adj[v2]) is not None:
            self.__adj[v2].getAdj().searchDelete(self.__adj[v1])
            self.__A -= 1

    def show(self):
        for i in range(self.__V):
            strOut = ""
            strOut += "Vértice: " + str(i) + " | Adjacências:"
            aux = self.__adj[i].getAdj().getFirst()
            while aux is not None:
                strOut += " " + str(aux.getVal())
                aux = self.__adj[i].getAdj().getNext()
            print(strOut)
            
    def numberAdj(self):
        return self.__A

    def numberVer(self):
        return self.__V

    
if __name__ == "__main__":
    g = GraphList(5)

    g.insertArc(0, 1)
    g.insertArc(0, 2)
    g.insertArc(1, 4)
    g.insertArc(2, 3)

    g.show()
