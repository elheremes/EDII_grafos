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

        g = aux.loadGraphList(argv[2], results)

        g.show()
        
        
            
if __name__ == "__main__":
    main(sys.argv)
