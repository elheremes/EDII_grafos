import DLList as dll


class Stack:
    def __init__(self):
        self.__elms = dll.DLinkedList()

    def push(self, data):
        self.__elms.insertEnd(data)

    def pop(self):
        return self.__elms.removeEnd()

    def size(self):
        return self.__elms.getNumElms()

    
