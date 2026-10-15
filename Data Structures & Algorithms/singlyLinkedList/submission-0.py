class LinkedList:
    
    def __init__(self):
        self.head: int = None
        self.tail: int = None
        self.linked_list: list[int] = []

    
    def get(self, index: int) -> int:
        try:
            elem = self.linked_list[index]
            return elem
        except IndexError:
            return -1

    def insertHead(self, val: int) -> None:
        self.linked_list.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.linked_list.append(val)

    def remove(self, index: int) -> bool:
        try:
            removed = self.linked_list.pop(index)
            return True
        except IndexError:
            return False
        

    def getValues(self) -> List[int]:
        return self.linked_list
        
