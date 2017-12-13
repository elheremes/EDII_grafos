import numpy as np
import DLList as dll


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
