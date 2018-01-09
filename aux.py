import GraphList as gl
import GraphMatrix as gm
import sys
import Word as wd

def isNumber(s):
    try:
        n = int(s)
        return True
    except ValueError:
        return False

def identifyGraphType(filename):
    results = {"oriented":False, "pondered":False}

    try:
        f = open(filename, "r")
    except FileNotFoundError:        
        print("Arquivo informado é inexistente, o programa irá abortar-se.")
        sys.exit()

    line = f.readline() # Pula primeira linha
    line = f.readline()

    numbers = 0
    for word in line.split():
        if isNumber(word):
            numbers += 1
        else:
            results["oriented"] = True

    if numbers == 3:
        results["pondered"] = True

    f.close()

    return results

def insertOrientation(g, v1, v2, orientation, p = 0):
    if orientation == ">":
        if p == 0:
            g.insertOrientedArc(v1, v2)
        else:
            g.insertOrientedArc(v1, v2, p)
    elif orientation == "<":
        if p == 0:
            g.insertOrientedArc(v2, v1)
        else:
            g.insertOrientedArc(v2, v1, p)
    elif orientation == "<>":
        if p == 0:
            g.insertOrientedArc(v1, v2)
            g.insertOrientedArc(v2, v1)
        else:
            g.insertOrientedArc(v1, v2, p)
            g.insertOrientedArc(v2, v1, p)

def insertOrientationM(g, v1, v2, orientation, p = 0):
    if orientation == ">":
        if p == 0:
            g.createAresta(v1, v2)
        else:
            g.createArestaPonderada(v1, v2, p)
    elif orientation == "<":
        if p == 0:
            g.createAresta(v2, v1)
        else:
            g.createArestaPonderada(v2, v1, p)
    elif orientation == "<>":
        if p == 0:
            g.createAresta(v1, v2)
            g.createAresta(v2, v1)
        else:
            g.createArestaPonderada(v1, v2, p)
            g.createArestaPonderada(v2, v1, p)
            
def loadGraphList(filename, gType):
    f = open(filename, "r")

    line = f.readline()

    if isNumber(line[0]) is False:
        print("Quantidade de Vértices Invalida, abortando.")
        sys.exit()

    graph = gl.GraphList(gType["pondered"])

    if gType["pondered"] is True:
        if gType["oriented"] is True:
            line = f.readline()
            while line != "":
                turn = 1
                for word in line.split():
                    if turn == 1:
                        v1 = word
                    if turn == 3:
                        v2 = word
                    if turn == 4:
                        wei = float(word)
                    if turn != 2 and turn != 4:
                        dado = wd.Word(word)
                        graph.insertVer(word, dado)
                    elif turn == 2:
                        orientation = word
                    turn += 1
                insertOrientation(graph, v1, v2, orientation, wei)
                line = f.readline()
        else:
            line = f.readline()
            while line != "":
                turn = 1
                for word in line.split():
                    if turn == 1:
                        v1 = word
                    if turn == 2:
                        v2 = word
                    if turn == 3:
                        wei = float(word)
                    if turn != 3:
                        dado = wd.Word(word)
                        graph.insertVer(word, dado)
                    turn += 1
                graph.insertArc(v1, v2, wei)
                line = f.readline()
    else:
        if gType["oriented"] is True:
            line = f.readline()
            orientation = "" # Necessário (?)
            while line != "":
                turn = 1
                for word in line.split():
                    if turn == 1:
                        v1 = word
                    if turn == 3:
                        v2 = word
                    if turn != 2:
                        dado = wd.Word(word)
                        graph.insertVer(word, dado)
                    else:
                        orientation = word
                    turn += 1
                insertOrientation(graph, v1, v2, orientation)
                line = f.readline()
        else:
            line = f.readline()
            orientation = "" # Necessário (?)
            while line != "":
                turn = 1
                for word in line.split():
                    if turn == 1:
                        v1 = word
                    elif turn == 2:
                        v2 = word
                    dado = wd.Word(word)
                    graph.insertVer(word, dado)
                    turn += 1
                graph.insertArc(v1, v2)
                line = f.readline()

    return graph

def loadGraphMatrix(filename, gType):
    f = open(filename, "r")

    line = f.readline()

    if isNumber(line) is False:
        print("Quantidade de Vértices Invalida, abortando.")
        sys.exit()
        
    graph = gm.GraphMatrix(int(line))
    
    if gType["pondered"] is True:
        if gType["oriented"] is True:
            line = f.readline()
            while line != "":
                turn = 1
                for word in line.split():
                    if turn == 1:
                        dado = gm.Vetex(wd.Word(word))
                        v1 = dado
                    if turn == 3:
                        dado = gm.Vetex(wd.Word(word))
                        v2 = dado
                    if turn == 4:
                        wei = float(word)
                    if turn != 2 and turn != 4:
                        status = graph.setVertexs(dado)
                        if status is True:
                            if turn == 1:
                                v1 = graph.getVertex(dado)
                            else:
                                v2 = graph.getVertex(dado)
                    elif turn == 2:
                        orientation = word
                    turn += 1
                insertOrientationM(graph, v1, v2, orientation, wei)
                line = f.readline()
        else:
            line = f.readline()
            while line != "":
                turn = 1
                for word in line.split():
                    if turn == 1:
                        dado = gm.Vetex(wd.Word(word))
                        v1 = dado
                    if turn == 2:
                        dado = gm.Vetex(wd.Word(word))
                        v2 = dado
                    if turn == 3:
                        wei = float(word)
                    if turn != 3:
                        status = graph.setVertexs(dado)
                        if status is True:
                            if turn == 1:
                                v1 = graph.getVertex(dado)
                            else:
                                v2 = graph.getVertex(dado)
                            
                    turn += 1
                graph.createArestaPonderada(v1, v2, wei)
                graph.createArestaPonderada(v2, v1, wei)
                line = f.readline()
    else:
        if gType["oriented"] is True:
            line = f.readline()
            orientation = "" # Necessário (?)
            while line != "":
                turn = 1
                for word in line.split():
                    if turn == 1:
                        dado = gm.Vetex(wd.Word(word))
                        v1 = dado
                    if turn == 3:
                        dado = gm.Vetex(wd.Word(word))
                        v2 = dado
                    if turn != 2:
                        status = graph.setVertexs(dado)
                        if status is True:
                            if turn == 1:
                                v1 = graph.getVertex(dado)
                            else:
                                v2 = graph.getVertex(dado)
                        
                    else:
                        orientation = word
                                
                    turn += 1
                insertOrientationM(graph, v1, v2, orientation)
                line = f.readline()
        else:
            line = f.readline()
            orientation = "" # Necessário (?)
            while line != "":
                turn = 1
                for word in line.split():
                    if turn == 1:
                        dado = gm.Vetex(wd.Word(word))
                        v1 = dado
                    elif turn == 2:
                        dado = gm.Vetex(wd.Word(word))
                        v2 = dado
                    status = graph.setVertexs(dado)
                    if status is True:
                        if turn == 1:
                            v1 = graph.getVertex(dado)
                        else:
                            v2 = graph.getVertex(dado)
                    turn += 1
                graph.createAresta(v1, v2)
                graph.createAresta(v2, v1)
                line = f.readline()

    return graph
