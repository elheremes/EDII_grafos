import sys
import aux
# import time
# import resource

def main(argv):
    if len(argv) < 2:
        print("Por favor, escolha o tipo de grafo que deseja usar. [GraphList = glist] ou [GraphMatrix = gmatrix]")
    elif len(argv) == 2:
        print("Por favor, escolha o arquivo de texto que será usado para carregar o grafo.")
    else:
        results = aux.identifyGraphType(argv[2])
        if argv[1] == "gmatrix":
            g = aux.loadGraphMatrix(argv[2], results)
            g.showMatriz()
            g.show()
            with open("nva.txt", "w") as myFile:
                myFile.write(str(g.numberVertexs()) + "\n")
                myFile.write(str(g.numberArestas()) + "\n")

            A = g.getNVertex(0)
            E = g.getNVertex(2)
            print(str(g.BFS(A)))
            print(str(g.DFS(A)))
            print(str(g.hasCicle()))
            g.algKruskal()
            # descomente para disjkar
            # g.dijkstra(A, E)
    
                
        elif argv[1] == "glist":
            g = aux.loadGraphList(argv[2], results)
            g.show()
            with open("nva.txt", "w") as myFile:
                myFile.write(str(g.numberVer()) + "\n")
                myFile.write(str(g.numberAdj()) + "\n")

            g.DFS("0")
    
            g.DFSwTime("0")
            
            g.BFS("0")     
            
            g.show()

            g.Kruskal()
                
            
if __name__ == "__main__":
    main(sys.argv)
