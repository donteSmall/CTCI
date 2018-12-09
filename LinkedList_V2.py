class Node(object):

    def __init__(self, data = None, next= None, prev= None):

        self.data =  data
        self.next = next
        self.prev = prev

    # def __str__(self):
    #
    #     return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_pointer_to_next(self, new_next):
        self.next = new_next

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

    def __repr__(self):
        return "--> " + str(self.data)

    def __str__(self):
        string = str(self.data)
        if self.next:
          string += ',' + str(self.next)
        return string


class linkedList(object):

    def __init__(self, head = None):
        self. tail = None
        self.head = head


        if head is not None:
            self.add_multiple(head)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


    def __str__(self):
        return ' -> '.join([str(x) for x in self])

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result +=1
            node = node.next
        return result

    def add(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

        return self.tail



    def add_multiple(self, data):

        for value in data:
            self.add(value)


    def __repr__(self):
        return str(self.head)

    def add_to_beginning(self,value):

        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head


    def return_size_of_list(self):
        current_item_in_list = self.head
        count = 0
        while current_item_in_list:
            count += 1
            current_item_in_list = current_item_in_list.get_next()
        return count


    #Searches list for a node containing the data and returns that node if found.
    def search(self, data):
        current_item_in_list = self.head
        found = False

        while current_item_in_list and found is False:
            if current_item_in_list.get_data() == data:
                return current_item_in_list
            else:
                current_item_in_list = current_item_in_list.get_next()
        if current_item_in_list is None:
            raise ValueError("Data not in list")
        return current_item_in_list
    #searches list for a node containing the requested data and
    #removes it from list if found.
    def delete(self, data):
        current_item_in_list = self.head
        previous = None
        found = False
        while current_item_in_list and found is False:

            if current_item_in_list.get_data() == data:
                found = True
            else:
                previous = current_item_in_list
                current_item_in_list = current_item_in_list.get_next()

        if current_item_in_list is None:
            raise ValueError("Data not in list")

        if previous is None:
            self.head = current_item_in_list.get_next()
        else:
            previous.set_pointer_to_next(current_item_in_list.get_next())


    def delete_middle(node):
        next = node.next
        node.data = node.data
        node.next = next.next

    def remove_duplicates(self):
            current_item_in_list = self.head
            while current_item_in_list is not None:
                runner = current_item_in_list
                while runner is not None:
                    prev = runner
                    runner = runner.get_next()
                    if runner is None:
                        break
                    if runner.get_data() == current_item_in_list.get_data():
                        next = runner.get_next()
                        prev.set_pointer_to_next(next)

                current_item_in_list = current_item_in_list.get_next()

    def remove_duplicates_2(self,head):
        node= head

        if node:
            values = {node.data: True}
            while node.next:
                if node.next.data in values:
                    node.next = node.next.next
                else:
                    values[node.next.data] = True
                    node = node.next
        return head

    def delete_middle(self,node):
        next = node.next
        node.data = node.data
        node.next = next.next

    def kth_to_last(self,head, k):
        lead,follow = head, head
        for _ in xrange(k):
            if not lead:
                return None
            lead = lead.next

        while lead:
            lead,follow = lead.next, follow.next

        return follow

    def partition(self,x):
        current = self.tail = self.head

        while current:
            next_node = current.next
            current.next = None
            if current.data < x:
                current.next = self.head
                self.head = current
            else:
                self.tail.next = current
                self.tail = current
            current = next_node

        if self.tail.next is not None:
            self.tail.next = None
        return self.head

    def sum_lists(self,llist1):
        p = self.head
        q = llist1.head
        sum_list = linkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.add(remainder)
            else:
                carry = 0
                sum_list.add(s)
            if p:
                p = p.next
            if q:
                q = q.next
        return sum_list




    def print_list(self):
        print("Print List.................")
        if self.head is None:
            return
        this_node = self.head
        print(this_node.to_string())

        while this_node.has_next():
            this_node = this_node.get_next()
            print(this_node.to_string())


#Prints out the values in a LinkedList

class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

#Original list
# a-> a->b-> c -> d -> e -> e
#Expected list
# a-> b-> c -> d -> e
class DoublyLinkedList(linkedList):
    def add(self, data):
        if self.head is None:
            self.tail = self.head = Node(data, None, self.tail)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        return self

# def main():
#     l = linkedList()
#     l.add_to_beginning("a")
#     l.add_to_beginning("a")
#     l.add_to_beginning("b")
#     l.add_to_beginning("c")
#     l.add_to_beginning("c")
#     l.add_to_beginning("c")
#     l.add_to_beginning("d")
#     l.add_to_beginning("e")
#     l.add_to_beginning("e")
#     l.search('d')
#     l.print_list()
#     l.remove_duplicates()
#     l.print_list()