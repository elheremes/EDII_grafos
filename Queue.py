import DLList as dll


class Queue:
    def __init__(self):
        self.__elms = dll.DLinkedList()

    def enqueue(self, data):
        self.__elms.insertStart(data)

    def dequeue(self):
        return self.__elms.removeStart()

    def size(self):
        return self.__elms.getNumElms()
