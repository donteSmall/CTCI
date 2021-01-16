import unittest
from Stack_DataStructure_03 import Stack, SetOfStack
from QueueViaStack_04 import QueueViaStacks_problem

class stackUnit_Tests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.setOfStack = SetOfStack(5)
        self.queue = QueueViaStacks_problem()


    def test_peek(self):
        self.stack.push('A')
        self.stack.push('B')
        self.stack.push('C')
        self.stack.push('D')


    def test_push(self):
        self.stack.push('A')
        self.stack.push('B')
        self.assertTrue(self.stack.get_stack()== ['A','B'])
        self.stack.push('C')
        self.assertTrue(self.stack.get_stack()== ['A','B','C'])

    def test_pop(self):
        self.stack.push('A')
        self.stack.push('B')
        self.stack.push('C')
        self.assertTrue(self.stack.get_stack()== ['A','B','C'])

        self.stack.pop()

        self.assertTrue(self.stack.get_stack()== ['A','B'])

    def test_is_paren_balanced(self):
    # (), ()(), (({[]}))  <- Balanced.
        self.assertTrue(self.stack.is_Pren_balanced("()"))
        self.assertFalse(self.stack.is_Pren_balanced("{{{)}]"))
        self.assertFalse(self.stack.is_Pren_balanced("[][]]]"))

    def test_is_paren_Not_balanced(self):
     #((), {{{)}], [][]]] <- Not Balanced.
        self.assertFalse(self.stack.is_Pren_balanced("[][]]]"))
        self.assertTrue(self.stack.is_Pren_balanced("()()"))
        self.assertTrue(self.stack.is_Pren_balanced("(({[]}))"))

    def test_len__(self):
        self.stack.push('A')
        self.stack.push('B')
        self.stack.push('C')
        self.stack.push('D')
        self.assertEqual(self.stack.__len__(),4)

    def test_queue_via_stacks(self):

        self.queue.add(11)
        self.queue.add(22)
        self.queue.add(33)
        self.assertEqual(self.queue.remove(), 11 )


if __name__ == '__main__':
    unittest.main()
