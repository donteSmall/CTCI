'''
A linked list is a chain of nodes, where each node contains
data and a pointer to the next node in the chain.
There’s a head pointer, which points to the first element of the linked list,
and if the list is empty then it simply points to null or nothing.

~ Freecodecamp
'''

class Node(object):
    def __init__(self, data, next =None, prev=None):
        self.data = data
        self.next= next
        self.prev= prev

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_pointer_next(self, next_node):
        self.next = next_node

    def has_next(self):
        if self.get_next is  None:
            return False
        return True
