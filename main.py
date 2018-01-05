import DLList as dll
import Word as wd

dado1 = wd.Word("Pedro")
dado2 = wd.Word("Abacate")
dado3 = wd.Word("Thiago")

lst = dll.DLinkedList()

lst.insertOrd(dado2)
# lst.insertOrd(dado1)
# lst.insertOrd(dado3)

print(lst)

# nd = lst.getFirst()
# while nd is not None:
#    print(nd)
#    nd = lst.getNext()

