from Stack_Data_Structure import Stack

class QueueViaStacks_problem(object):
    def __init__(self):
        self.inside_stack = Stack()
        self.outside_stack = Stack()

    def add(self, item):
        self.inside_stack.push(item)

    def remove(self):
        if len(self.outside_stack) == 0:
            while len(self.inside_stack):
                self.outside_stack.push(self.inside_stack.pop_())
        return self.outside_stack.pop_()
