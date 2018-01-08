import numpy as np
import Word as wd
import DLList as dll
import Stack as st
import Queue as qe

class Aresta:
    def __init__(self, v1, v2, peso):
        self.__v1 = v1 
        self.__v2 = v2 
        self.__peso = peso

    def __str__(self):
        outstr = "v1: "
        outstr += str(self.__v1) + " / v2: "
        outstr += str(self.__v2) + " / peso: "
        outstr += str(self.__peso)

        return outstr
    
    def getPeso(self):
        return self.__peso

    def getV1(self):
        return self.__v1

    def getV2(self):
        return self.__v2

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
        self.__arestas = []

    def getVetArestas(self):
        return self.__arestas

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

    ########################################################################################################
    # 0 Branco, 1 Cinza, 2 Preto
    def BFS(self, start):
        caminho = ""
        time = 0
        start.setColor(1)
        start.setTime(time)
        caminho += start.getKey().getVal()
        f = qe.Queue()
        f.enqueue(start)
        while f.size() > 0:
            time = time + 1
            elm = f.first()
            aux = self.adjacente(elm)

            if aux != None :
                if aux.getColor() == 0:
                    aux.setColor(1)
                    aux.setTime(time)
                    caminho += " -> " + aux.getKey().getVal()
                    f.enqueue(aux)
                else :
                    aux.setColor(2)
                    f.dequeue()
            else :
                f.dequeue()

        return caminho

    def DFS(self, start):
        caminho = ""
        time = 0
        start.setColor(1)
        start.setTime(time)
        caminho += start.getKey().getVal()
        p = st.Stack()
        p.push(start)
        while p.size() > 0:
            time = time + 1
            elm = p.top()
            aux = self.adjacente(elm)

            if aux != None :
                if aux.getColor() == 0:
                    aux.setColor(1)
                    aux.setTime(time)
                    caminho += " -> " + aux.getKey().getVal()
                    p.push(aux)
                else :
                    aux.setColor(2)
                    p.pop()
            else :
                p.pop()

        return caminho

    ########################################################################################################    
    def grau(self, index):
        numIndex = self.index(index)
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
        
        for i in range(self.__V):
            for j in range(self.__V):
                if markedCell[i][j] != 0:
                    print("Edge: " + str(i) + " -- " + str(j) + " // Weight: " + str(self.__adj[i][j]));

    ########################################################################################################
    def buscaKruskal(self, subset, vertex):
        if subset[int(vertex)] == -1 :
            return vertex
        else :
            return self.buscaKruskal(subset, subset[int(vertex)])
           
    def union(self, subset, v1, v2):
        v1set = self.buscaKruskal(subset, v1)
        v2set = self.buscaKruskal(subset, v2)
        subset[int(v1set)] = v2set
 
    def hasCicle(self):
        subset = np.zeros(self.__V)
        for i in range(self.__V):
            subset[i] = -1

        for i in range(self.__V):
            for j in range(i, self.__V):
                if self.__adj[i][j] != 0 :
                    v1 = self.buscaKruskal(subset, i)
                    v2 = self.buscaKruskal(subset, j)

                    if v1 == v2 :
                        return True
                    else:
                        self.union(subset, v1, v2)
        return False

    def sortAresta(self):
        for i in range(len(self.__arestas)):
            for j in range(i, len(self.__arestas)):
                if i != j:
                    if self.__arestas[i].getPeso() > self.__arestas[j].getPeso() :
                        self.__arestas[i], self.__arestas[j] = self.__arestas[j], self.__arestas[i]  

    def generateArestaForMST(self):
        for i in range(self.__V):
            for j in range(self.__V):
                if self.__adj[i][j] != 0 :
                    self.__arestas.append(Aresta(i, j, self.__adj[i][j]))
    
    def algKruskal(self):
        subset = np.zeros(self.__V)
        mst = []
        self.generateArestaForMST()
        self.sortAresta()

        for i in range(self.__V):
            subset[i] = -1

        for i in range(len(self.__arestas)):
            v1 = self.buscaKruskal(subset, self.__arestas[i].getV1())
            v2 = self.buscaKruskal(subset, self.__arestas[i].getV2())
            
            if v1 != v2 :
                mst.append(self.__arestas[i])
                self.union(subset, v1, v2)

        for i in range(len(mst)):
            print(" v " + str(mst[i].getV1()) + " -- " + str(mst[i].getV2()) + " peso: " + str(mst[i].getPeso()))

        return mst

    ########################################################################################################
    def dijkstra(self, start, end):
        dist = np.zeros(self.__V)
        visited = np.zeros(self.__V)
        f = qe.Queue()
        inf = 9999  

        for i in range(self.__V):
            dist[i] = inf
            visited[i] = False
        
        dist[self.index(start)] = 0
        f.enqueue(start)

        while f.size() > 0 :
            aux = f.dequeue()
            print("dist: " + str(dist))
            print("visited: " + str(visited))
            print("fila: " + str(f))
            input()
            if visited[self.index(aux)] == False :
                visited[self.index(aux)] = True

                for i in range(self.__V):
                    if self.__adj[self.index(aux)][i] != 0 :
                        vetAdj = i
                        custoAresta = self.__adj[self.index(aux)][i]

                        if dist[vetAdj] > (dist[self.index(aux)] + custoAresta) : 
                            dist[vetAdj] = dist[self.index(aux)] + custoAresta
                            f.enqueue(self.__vertexs[vetAdj])

        print("custo: " + str(dist[self.index(end)]))
        return dist[self.index(end)]
    
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

    g.createArestaPonderada(A, B, 5)
    g.createArestaPonderada(A, C, 6)
    g.createArestaPonderada(A, D, 7)
    g.createArestaPonderada(B, E, 4)
    g.createArestaPonderada(D, E, 1)
    g.createArestaPonderada(C, D, 5)

    #g.showMatriz()
    # g.algPrim(A)
    #print(str(g.BFS(A)))
    #print(str(g.DFS(A)))
    #print(str(g.hasCicle()))
    g.algKruskal()
    #g.dijkstra(A, E)
    
