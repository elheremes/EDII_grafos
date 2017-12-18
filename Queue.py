import DLList as dll

class Queue:
    def __init__(self):
        self.__elms = dll.DLinkedList()

    def __str__(self):
        return self.__elms.__str__()
        
    def enqueue(self, data):
        self.__elms.insertEnd(data)
        
    def dequeue(self):
        return self.__elms.removeStart()

    def size(self):
        return self.__elms.lenght()