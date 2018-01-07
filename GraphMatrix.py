import numpy as np
import Word as wd
import DLList as dll
import Stack as st
import Queue as qe

class Vetex:
    def __init__(self, key):
        self.__time = 0 #pegar o tempo
        self.__color = 0 #setar a cor
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

    def createArestaPonderada(self, v1, v2, peso):
        posV1 = self.index(v1)
        posV2 = self.index(v2)
        if self.__adj[posV1, posV2] == 0:
            self.__adj[posV1, posV2] = peso
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
                if self.__adj[line, i] != 0 and tmp[i].getColor() == 0:
                    return tmp[i]

            return None

    # 0 Branco, 1 Cinza, 2 Preto
    def BFS(self, start, key):
        caminho = ""
        time = 0
        start.setColor(1)

        if start.getKey().getVal() == key:
            start.setTime(time)
            caminho += start.getKey().getVal()
            return caminho

        start.setTime(time)
        caminho += start.getKey().getVal()
        f = qe.Queue()
        f.enqueue(start)
        while f.size() > 0:
            input()
            print(f)
            time = time + 1
            elm = f.first()
            aux = self.adjacente(elm)
            #print(aux.getVal())

            if aux != None :
                if aux.getColor() == 0:
                    aux.setColor(1)
                    aux.setTime(time)
                    caminho += " -> " + aux.getKey().getVal()
                    if aux.getKey().getVal() == key:
                        print(caminho)
                        return caminho
                    f.enqueue(aux)
                else :
                    aux.setColor(2)
                    f.dequeue()
            else :
                f.dequeue()

        return "Not Found!"

    def DFS(self, start, key):
        caminho = ""
        time = 0
        start.setColor(1)

        if start.getKey().getVal() == key:
            start.setTime(time)
            caminho += start.getKey().getVal()
            return caminho

        start.setTime(time)
        caminho += start.getKey().getVal()
        p = st.Stack()
        p.push(start)
        while p.size() > 0:
            #input()
            #print(p)
            time = time + 1
            elm = p.top()
            aux = self.adjacente(elm)

            if aux != None :
                if aux.getColor() == 0:
                    aux.setColor(1)
                    aux.setTime(time)
                    caminho += " -> " + aux.getKey().getVal()
                    if aux.getKey().getVal() == key:
                        return caminho
                    p.push(aux)
                else :
                    aux.setColor(2)
                    p.pop()
            else :
                p.pop()

        return "Not Found!"
    
    def grau(self, index):
        numIndex = self.index(index)
        numGrau = 0
        for i in range(self.__V):
            if self.__adj[numIndex][i] != 0 :
                numGrau = numGrau + 1
        
        return numGrau

    def grau(self, numIndex):
        numGrau = 0
        for i in range(self.__V):
            if self.__adj[numIndex][i] != 0 :
                numGrau = numGrau + 1
        
        return numGrau

    def algPrim(self, start):
        inf     = 9999
        solved = True
        markedCell = np.zeros((self.__V, self.__V))
        markedVertex = np.zeros(self.__V)
        markedVertex[0] = 1

        while solved :
            menorPeso = inf
            count = 0
            expectedR = -1
            expectedL = -1

            for i in range(self.__V):
                if markedVertex[i] == 1 :
                    for j in range(self.__V):
                        if self.__adj[i][j] != 0 and self.__adj[i][j] < menorPeso and markedCell[i][j] == 0:
                            menorPeso = self.__adj[i][j]
                            expectedR = i
                            expectedL = j

            if expectedR != -1 and expectedL != -1  :
                markedCell[expectedR][expectedL] = 1
                markedCell[expectedL][expectedR] = 1
                markedVertex[expectedR] = 1
                markedVertex[expectedL] = 1

            for i in range(self.__V) :
                if markedVertex[i] :
                    count = count + 1
            if count == self.__V :
                solved = False

    def algKruskal(self, start):
        pass

if __name__ == "__main__":
    g = GraphMatrix(8)

    R = Vetex(wd.Word("R"))
    S = Vetex(wd.Word("S"))
    T = Vetex(wd.Word("T"))
    U = Vetex(wd.Word("U"))
    V = Vetex(wd.Word("V"))
    W = Vetex(wd.Word("W"))
    X = Vetex(wd.Word("X"))
    Y = Vetex(wd.Word("Y"))

    g.setVertexs(R)
    g.setVertexs(S)
    g.setVertexs(T)
    g.setVertexs(U)
    g.setVertexs(V)
    g.setVertexs(W)
    g.setVertexs(X)
    g.setVertexs(Y)

    g.createAresta(V, R)
    g.createAresta(R, S)
    g.createAresta(S, W)
    g.createAresta(W, T)
    g.createAresta(W, X)
    g.createAresta(T, X)
    g.createAresta(T, U)
    g.createAresta(U, X)
    g.createAresta(U, Y)
    g.createAresta(X, Y)

    g.showMatriz()
    #g.algPrim(A)
    g.BFS(V, "Y")
