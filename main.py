import DLList as dll
import Word as wd

dado1 = wd.Word("Myrlla")
dado2 = wd.Word("Milennyr")
dado3 = wd.Word("Pedro")

lst = dll.DLinkedList()

lst.insertStart(dado1)
lst.insertStart(dado2)
lst.insertStart(dado3)

print(lst)
