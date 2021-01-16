import unittest, random
class Node():
    def __init__(self, data=None, left= None, right= None):
        self.data, self.left, self.right = data, left,right

        self.count =1

        if self.left:
            self.count += self.left.count
        if self.right:
            self.count += self.right.count

    def get_random_node(self):
        return self.get_numbered_node(random.randint(0, self.count - 1))
        #Wiil return random number from a numbered node

    def get_numbered_node(self,number):
        if number == 0 :
            return self

        if self.left:
            if number - 1 < self.left.count:
                return self.left.get_numbered_node(number - 1)
            elif self.right:
                return self.right.get_numbered_node(number - 1 - self.left.count)
        if self.right:
            return self.right.get_numbered_node(number -1 )
        return None

    random_val = False

    def randomint(lower_bound, upper_bound):
        if not mock_random_val is False:
            return mock_random_val
        return random.randint(lower_bound,upper_bound)
