class dllNode:
    def __init__(self, data, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

    def getPrev(self):
        return self.__prev

    def setPrev(self, prev):
        self.__prev = prev


class DLinkedList:
    def __init__(self):
        self.__root = None
        self.__nElms = 0

    def __str__(self):
        outstr = "<-- "

        aux = self.__root
        while aux is not None and aux.getNext() is not self.__root:
            outstr += str(aux.getData().getVal()) + " <--> "
            aux = aux.getNext()

        outstr += str(aux.getData().getVal()) + " --> "

        return outstr

    def insertEnd(self, data):
        if self.__root is None:
            self.__root = dllNode(data)
        else:
            newNode = dllNode(data)
            
            if self.__nElms == 1:
                self.__root.setPrev(newNode)
                self.__root.setNext(newNode)
                newNode.setPrev(self.__root)
                newNode.setNext(self.__root)
            else:
                last = self.__root.getPrev()
                self.__root.setPrev(newNode)
                last.setNext(newNode)
                newNode.setPrev(last)
                newNode.setNext(self.__root)
                
        self.__nElms += 1

    def insertStart(self, data):
        if self.__root is None:
            self.__root = dllNode(data)
        else:
            newNode = dllNode(data)

            if self.__nElms == 1:
                self.__root.setPrev(newNode)
                self.__root.setNext(newNode)
                newNode.setPrev(self.__root)
                newNode.setNext(self.__root)
            else:
                newNode.setNext(self.__root)
                newNode.setPrev(self.__root.getPrev())
                last = self.__root.getPrev()
                self.__root.setPrev(newNode)
                last.setNext(newNode)

            self.__root = newNode

        self.__nElms += 1

    def removeEnd(self):
        if self.__root is None:
            return None

        if self.__nElms == 1:
            node = self.__root
            self.__root = None
        elif self.__nElms == 2:
            node = self.__root.getNext()
            self.__root.setNext(None)
            self.__root.setPrev(None)
        else:
            node = self.__root.getPrev()
            last = node.getPrev()
            last.setNext(self.__root)
            self.__root.setPrev(last)

        self.__nElms -= 1
        return node.getData()

    def removeStart(self):
        if self.__root is None:
            return None

        if self.__nElms == 1:
            node = self.__root
            self.__root = None
        elif self.__nElms == 2:
            node = self.__root
            self.__root = self.__root.getNext()
            self.__root.setNext(None)
            self.__root.setPrev(None)
        else:
            node = self.__root
            self.__root = self.__root.getNext()
            self.__root.setPrev(node.getPrev())

        self.__nElms -= 1
        return node.getData()

    def search(self, key):
        node = self.__root

        while node is not None:
            if node.getData().getVal() == key:
                return node.getData()
            node = node.getNext()

        return None

    def getNumElms(self):
        return self.__nElms
