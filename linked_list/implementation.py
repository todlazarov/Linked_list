from interface import AbstractLinkedList
from node import Node
from copy import deepcopy


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=[]):
        self.start = None
        self.end = None
        
        for element in elements:
            self.append(element)

    def __str__(self):
        items = ", ".join(str(item) for item in self)
        
        return "[" + items + "]"

    def __len__(self):
        return reduce(lambda x,y: x+1, [item for item in self], 0)

    def __iter__(self):
        current = self.start
        while not current is None:
            yield current
            current = current.next
        raise StopIteration()

    def __getitem__(self, index):
        if index < 0 or index > len(self)-1:
            raise IndexError("The index is out of range")
            
        for idx, node in enumerate(self):
            if idx == index:
                return node

    def __add__(self, other):
        new_linked_list = LinkedList()
        
        for node in self:
            new_linked_list.append(node.elem)
        for node in other:
            new_linked_list.append(node.elem)
            
        return new_linked_list

    def __iadd__(self, other):
        for node in other:
            self.append(node.elem)
        return self

    def __eq__(self, other):
        if len(self) != len(other):
            return False
            
        return not False in [list1 == list2 for list1, list2 in zip(self, other)]
    
    def __ne__(self, other):
        return not self == other

    def append(self, elem):
        temp = Node(elem)
        
        if len(self) == 0:
            self.start = temp
            self.end = temp
        else:
            self.end.next = temp
            self.end = self.end.next

    def count(self):
        return len(self)

    def pop(self, index=None):
        if index is None:
            index = len(self)-1
        pop_node = self[index]
        
        if len(self) == 1:
            self.start = None
            self.end = None
        elif pop_node is self.start:
            self.start = pop_node.next
        else:
            if pop_node is self.end:
                self.end = self[index-1]
            self[index-1].next = pop_node.next
            
        return pop_node.elem