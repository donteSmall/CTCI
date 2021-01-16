'''
A linked list is a chain of nodes, where each node contains
data and a pointer to the next node in the chain.
There’s a head pointer, which points to the first element of the linked list,
and if the list is empty then it simply points to null or nothing.

1->2->3->4->5->Null
'''
class Node(object):
    def __init__(self,data= None, next=None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_pointer_next(self, next_node):
        self.next= next_node

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

class linkedlist(object):
    def __init__(self,head= None, tail= None):
        self.head = head
        self.tail = tail
        
    def __iter__(self):
        node = self.head
        while node:
            yeild node
            node = node.next

    def __str__(self):
        return ","join(str(x) for x in self)

    def __len__(self):
        count = 0
        is_node = self.head
        while is_node:
            count +=1
            is_node = is_node.next
        return count

    def add(self,data):
        is_node= self.head
        if is_node is None:
            self.tail = self.head = node(data)
        else:
            self.tail.next = node(data)
            self.tail = self.tail.next

    def add_muliple(self, data):
        for value in data:
            self.add(value)
