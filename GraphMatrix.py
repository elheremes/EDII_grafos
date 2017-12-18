import numpy as np
import Word as wd
import DLList as dll
import Stack as st

class Vetex:
    def __init__(self, key):
        self.__time = 0#pegar o tempo
        self.__color = 0#setar a cor
        self.__key = key 

    def setTime(self, time):
        self.__time = time

    def getTime(self):
        return self.__time

    def getPos(self):
        return self.__pos

    def getColor(self):
        return self.__color

    def getKey(self):
        return self.__key

    def setColor(self, color):
        self.__color = color

    def getVal(self):
        return self.__key.getVal()

class GraphMatrix:
    def __init__(self, V):
        if V <= 0:
            V = 1
        self.__V = V
        self.__A = 0
        self.__adj = np.zeros((self.__V, self.__V))
        self.__vertexs = []

    def getVertexs(self):
        return self.__vertexs

    def setVertexs(self, Vetex):
        self.__vertexs.append(Vetex)

    def index(self, key):
        for i in range(len(self.__vertexs)):
            if self.__vertexs[i] == key :
                return i

    def createAresta(self, v1, v2):
        posV1 = self.index(v1)
        posV2 = self.index(v2)
        if self.__adj[posV1, posV2] == 0:
            self.__adj[posV1, posV2] = 1
            self.__A += 1

    def deleteAresta(self, v1, v2):
        posV1 = self.index(v1)
        posV2 = self.index(v2)
        if self.__adj[posV1, posV2] == 1:
            self.__adj[posV1, posV2] = 0
            self.__A -= 1

    def show(self):
        for i in range(self.__V):
            strOut = ""
            strOut += "Vértice: " + str(i) + " | Adjacências:"
            for j in range(self.__V):
                if self.__adj[i, j] == 1:
                    strOut += " " + str(j)
            print(strOut)

    def showMatriz(self):
        matOut = ""
        for i in range(0, self.__V):
            for j in range(0, self.__V):
                matOut += "[" + str(self.__adj[i, j]) + "]" + " "
            matOut += "\n" 
        print(matOut)

    def numberArestas(self):
        return self.__A

    def numberVertexs(self):
        return self.__V

    def adjacente(self, v):
        if v != None:
            tmp = self.__vertexs
            line = tmp.index(v)
            for i in range(self.__V):
                if self.__adj[line, i] == 1 :#and tmp[i].getColor() != 2:
                    return tmp[i]
            
            return None

    # 0 Branco, 1 Cinza, 2 Preto
    def DFS(self, start, key):
        caminho = ""
        time = 0
        start.setColor(1)

        if start.getKey().getVal() == key:
            caminho += start.getKey().getVal()
            return caminho

        caminho += start.getKey().getVal()
        p = st.Stack()
        p.push(start)
        while p.size() > 0:
            elm = p.top()
            aux = self.adjacente(elm)

            if aux != None :
                if aux.getColor() == 0 :
                    aux.setColor(1)
                    p.push(aux)
                    caminho += " -> " + aux.getKey().getVal()
                    if aux.getKey().getVal() == key :
                        return caminho
                else:
                    aux.setColor(2)
                    p.pop()   
        
        return "Not Found!" 

if __name__ == "__main__":
    g = GraphMatrix(5)
    
    A = Vetex(wd.Word("A"))
    B = Vetex(wd.Word("B"))
    C = Vetex(wd.Word("C"))
    D = Vetex(wd.Word("D"))
    E = Vetex(wd.Word("E"))

    g.setVertexs(A)
    g.setVertexs(B)
    g.setVertexs(C)
    g.setVertexs(D)
    g.setVertexs(E)

    g.createAresta(A, B)
    g.createAresta(A, E)
    g.createAresta(B, C)
    g.createAresta(C, D)
    g.createAresta(C, A)

    print(g.DFS(A, "D"))
    #g.showMatriz()