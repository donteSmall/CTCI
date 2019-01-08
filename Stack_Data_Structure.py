class Node(object):
    def __init__(self,value):
        self.value = value
        self.above = None
        self.below = None


class Stack(object):
    def __init__(self,capacity= None):
        self.items= []
        self.value= None
        self.top = None
        self.bottom = None
        self. size = 0

        # if capacity < 6:
        #     raise NameError("A stack is greater than one")
        # else:
        self.capacity = capacity
    def push(self,item):
        self.items.append(item)
    def is_Full(self):
        return self.size == self.capacity
    def pop(self):
        if self.items == []:
            raise NameError("Can't pop an empty stack")
        else:
            popped_data = self.items[-1][-1]
        if len(self.items[-1])== 1:

            del self.items[-1]
        else:
            del self.items[-1][-1]
        return popped_data
    def pop_(self):
        if not self.top:
            return None
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value


    def popAt(self, index):
        if self.items == []:
            raise NameError("Can't pop an empty staack")

        elif index -1 > len(self.items):
            raise NameError("Index is out of range")
        else:
            popped_data = self.items[index-1][-1]
            if len(self.items[index-1]) == 1:
                del self.items[-1]
            elif len(self.items)==index:
                del self.stacks[-1][-1]
            else:
                self.items[index-1][-1] = self.items[index][0]

                for i in range(index, len(self.items)):
                    for j in range(0,len(self.items[i]-1)):
                        self.items[i][j] = self.items[i][j+1]
                    if i < len(self.items)-1:
                        self.items[i][-1] = self.items[i+1][0]
                del self.items[-1][-1]

                if len(self.items[-1]) == 0:
                    del self.items[-1]
        return popped_data

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_Match(self,p1,p2):
        if p1 == "(" and p2 == ")":
            return True
        elif p1 == "{" and p2 == "}":
            return True
        elif p1 == "[" and p2 == "]":
            return True
        else:
            return False
    def __len__(self):
        return len(self.items)

    def is_pren_balanced(self,paren_string):
        is_balanced = True
        indx= 0
        while indx < len(paren_string) and is_balanced:
            paren= paren_string[indx]
            if paren in "([{":
                self.push(paren)
            else:
                if self.is_empty():
                    is_balanced = False
                else:
                    top = self.pop()
                    if not self.is_Match(top, paren):
                        is_balanced = False
            indx+=1
        if self.is_empty and is_balanced:
            return True
        else:
            return False

class SetOfStack(object):
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []

    def get_last_stack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]

    def is_empty(self):
        last = self.get_last_stack()
        return not last or last.is_empty()

    def push(self,value):
        last= self.get_last_stack()

        if last and not last.is_Full():
            last.push(value)
        else:
            stack = Stack(self.capacity)
            stack.push(value)
            self.stacks.append(stack)
    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None
        value = last.pop()
        if last.size ==0:
            del self.stacks[-1]
            return value
    def pop_at(self, index):
        return self.left_shift(index, True)

    def left_shift(self, index, remove_top):
        stack= self.stacks[index]
        removed_item = stack.pop_() if remove_top else stack.remove_bottom()
        if stack.is_empty():
            del self.stacks[index]
        elif len(self.stacks) > index + 1:
            value = self.left_shift(index + 1 , False)
            stack.push(value)
        return removed_item






#s = Stack()
# print(s.is_empty())
# s.push('A')
# s.push('B')
# print(s.get_stack())
# s.push('C')
# print(s.get_stack())
# s.pop()
# print(s.get_stack())
