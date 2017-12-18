import DLList as dll

class Stack:
    def __init__(self):
        self.__elms = dll.DLinkedList()

    def __str__(self):
    	return self.__elms.__str__()

    def push(self, data):
        self.__elms.insertEnd(data)

    def pop(self):
        return self.__elms.removeEnd()

    def top(self):
    	return self.__elms.getLast()

    def size(self):
        return self.__elms.lenght()