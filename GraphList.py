import numpy as np
import DLList as dll
import Queue as qu
import Word as wd
import Stack as stk

class ArcNode:
    def __init__(self, data, source, oriented=False, w=1):
        self.__data = data
        self.__weight = w  # PESO
        self.__oriented = oriented
        self.__source = source

    def __str__(self):
        return str(self.__weight)
        
    def getVal(self):
        return self.__data.getVal()

    def getData(self):
        return self.__data.getData()

    def setVal(self, val):
        self.__data.setVal(val)

    def getAdj(self):
        return self.__data.getAdj()

    def getWeight(self):
        return self.__weight

    def getSource(self):
        return self.__source
        
    def VertexForm(self):
        return self.__data

    def Oriented(self):
        return self.__oriented
    
class VertexNode:
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
            self.__adj = {i: VertexNode(i) for i in range(self.__V)}
        else:
            self.__adj = {}
        # listAux = [VertexNode(i) for i in range(self.__V)]
        # self.__adj = np.array(listAux)
        # seria melhor aqui uma HashTable?

        # Verificar logo aqui e colocar atributos dizendo se vai ser
        # ponderado ou não, e se vai ser direcionado ou não

    def degree(self, v): # GRAU
        return self.__adj[v].getAdj().getNelms()
        
    def insertVer(self, v, value):
        if v in self.__adj:
            self.__adj[v].setVal(value)
        else:
            self.__adj[v] = VertexNode(v, value)
            self.__V += 1
            
    def insertArc(self, v1, v2, w=1):
        if self.__adj[v1].getAdj().search(self.__adj[v2]) is None:
            self.__adj[v1].getAdj().insertOrd(ArcNode(self.__adj[v2], v1, False, w))
            self.__adj[v2].getAdj().insertOrd(ArcNode(self.__adj[v1], v2, False, w))
            self.__A += 1
            # += 2? Não?
            
    def deleteArc(self, v1, v2):
        if self.__adj[v1].getAdj().searchDelete(
                self.__adj[v2].getVal())is not None:
            self.__adj[v2].getAdj().searchDelete(self.__adj[v1].getVal())
            self.__A -= 1

    def insertOrientedArc(self, v1, v2, w=1):
        if self.__adj[v1].getAdj().search(self.__adj[v2]) is None:
            self.__adj[v1].getAdj().insertOrd(ArcNode(self.__adj[v2], v1, True, w))
            self.__A += 1

    def deleteOrientedArc(self, v1, v2):
        if self.__adj[v1].getAdj().searchDelete(
                self.__adj[v2].getVal())is not None:
            self.__A -= 1
            # return True # ?
            
    def show(self):
        for key in self.__adj:
            strOut = ""
            strOut += "Vértice: " + str(key) + " | Adjacências:"
            aux = self.__adj[key].getAdj().getFirst()
            while aux is not None:
                if aux.Oriented() is True:
                    strOut += " " + str(aux.getVal()) + " --> " + str(aux.getWeight()) + " |"
                else:
                    strOut += " " + str(aux.getVal()) + " :-: " + str(aux.getWeight()) + " |"
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
            if ptr is not None:
                ptr = ptr.VertexForm()
            while ptr is not None:
                if color[ptr] == 0:
                    color[ptr] = 1
                    dist[ptr] = dist[u] + 1
                    pred[ptr] = u
                    Q.enqueue(ptr)
                ptr = self.__adj[u.getVal()].getAdj().getNext()
                if ptr is not None:
                    ptr = ptr.VertexForm()
            color[u] = 2

    def DFS(self, s):
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
        Q = stk.Stack()
        Q.push(s)
        while Q.size() != 0:
            print(Q)
            u = Q.pop()
            ptr = self.__adj[u.getVal()].getAdj().getFirst()
            if ptr is not None:
                ptr = ptr.VertexForm()
            while ptr is not None:
                if color[ptr] == 0:
                    color[ptr] = 1
                    dist[ptr] = dist[u] + 1
                    pred[ptr] = u
                    Q.push(ptr)
                ptr = self.__adj[u.getVal()].getAdj().getNext()
                if ptr is not None:
                    ptr = ptr.VertexForm()
            color[u] = 2

    def DFSwTime(self, s):
        color = {}
        dist = {}
        pred = {}
        d = {}
        f = {}
        time = 0
        
        for key, item in self.__adj.items():
            color[item] = 0
            dist[item] = -1
            pred[item] = None

        if s in self.__adj:
            s = self.__adj[s]
        else:
            return None

        for key in color:
            if color[key] == 0:
                time = self.__DFSwTimeVisit(s, time, color, dist, pred, d, f)

        return time

    def __DFSwTimeVisit(self, v, time, color, dist, pred, d, f):
        color[v] = 1
        time = time + 1
        d[v] = time
        ptr = self.__adj[v.getVal()].getAdj().getFirst()
        if ptr is not None:
            ptr = ptr.VertexForm()
        while ptr is not None:
            if color[ptr] == 0:
                time = self.__DFSwTimeVisit(ptr, time, color, dist, pred, d, f)
            ptr = self.__adj[v.getVal()].getAdj().getNext()
            if ptr is not None:
                ptr = ptr.VertexForm()
                
        color[v] = 2
        time = time + 1
        f[v] = time

        print(d[v], f[v])
        
        return time

    def buscaKruskal(self, subset, vertex):
        if subset[vertex] == -1:
            return vertex
        else:
            return self.buscaKruskal(subset, subset[vertex])
    
    def union(self, subset, v1, v2):
        v1set = self.buscaKruskal(subset, v1)
        v2set = self.buscaKruskal(subset, v2)
        subset[v1set] = v2set
    
    def hasCircle(self):
        subset = {}
        for item in self.__adj:
            subset[self.__adj[item].getVal()] = -1

        for item in self.__adj:
            ptr = self.__adj[item].getAdj().getFirst()
            while ptr is not None:
                v1 = self.buscaKruskal(subset, self.__adj[item].getVal())
                v2 = self.buscaKruskal(subset, ptr.getVal())

                if v1 == v2:
                    return True
                else:
                    self.union(subset, v1, v2)
                
                ptr = self.__adj[item].getAdj().getNext()

        return False

    def sortAresta(self, arestas):
        for i in range(len(arestas)):
            for j in range(i, len(arestas)):
                if i != j:
                    if arestas[i].getWeight() > arestas[j].getWeight():
                        arestas[i], arestas[j] = arestas[j], arestas[i]
        return arestas
    
    def generateArestaForMST(self):
        arestas = []
        for item in self.__adj:
            ptr = self.__adj[item].getAdj().getFirst()
            while ptr is not None:
                arestas.append(ptr)
                ptr = self.__adj[item].getAdj().getNext()

        return arestas

    def Kruskal(self):
        subset = {}
        mst = []
        arestas = self.generateArestaForMST()
        arestas = self.sortAresta(arestas)

        for item in self.__adj:
            subset[self.__adj[item].getVal()] = -1

        for i in range(len(arestas)):
            v1 = self.buscaKruskal(subset, arestas[i].getSource())
            v2 = self.buscaKruskal(subset, arestas[i].getVal())

            if v1 != v2:
                mst.append(arestas[i])
                self.union(subset, v1, v2)

        for i in range(len(mst)):
             print(" v " + str(mst[i].getSource()) + " -- " + str(mst[i].getVal()) + " peso: " + str(mst[i].getWeight()))

        return mst
            
    
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
    
    g.insertArc("s", "w", 5)
    g.insertArc("s", "r", 2)
    g.insertArc("r", "v", 3)
    g.insertArc("w", "t", 4)
    g.insertArc("w", "x", 2)
    g.insertArc("t", "u", 3)
    g.insertArc("t", "x", 8)
    g.insertArc("x", "y", 5)
    g.insertArc("x", "u", 11)
    g.insertArc("u", "y", 2)

    # g.insertOrientedArc("s", "w", 5)
    # g.insertOrientedArc("w", "t", 2)
    # g.insertOrientedArc("t", "v")
    # g.insertOrientedArc("w", "x")
    # g.insertOrientedArc("t", "u", 3)
    # g.insertOrientedArc("t", "x")
    # g.insertOrientedArc("x", "y")
    # g.insertOrientedArc("x", "u")
    # g.insertOrientedArc("u", "y")
    g.DFS("s")
    
    g.DFSwTime("s")
    
    g.BFS("s")     

    g.show()

    g.Kruskal()
    
    # arestas = g.generateArestaForMST()

    # for i in range(len(arestas)):
    #     print(arestas[i])

    # arestas = g.sortAresta(arestas)

    # print("\n")

    # for i in range(len(arestas)):
    #     print(arestas[i])

    
    
    # print(g.degree("s"))

    # print(g.hasCircle())
