import unittest
from Stack_Data_Structure import Stack,SetOfStack

class stackUnit_Tests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.setOfStack = SetOfStack(5)

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
        self.assertTrue(self.stack.is_pren_balanced("()"))
        self.assertFalse(self.stack.is_pren_balanced("{{{)}]"))
        self.assertFalse(self.stack.is_pren_balanced("[][]]]"))

    def test_is_paren_Not_balanced(self):
     #((), {{{)}], [][]]] <- Not Balanced.
        self.assertFalse(self.stack.is_pren_balanced("[][]]]"))
        self.assertTrue(self.stack.is_pren_balanced("()()"))
        self.assertTrue(self.stack.is_pren_balanced("(({[]}))"))

    def test_len__(self):
        self.stack.push('A')
        self.stack.push('B')
        self.stack.push('C')
        self.stack.push('D')
        self.assertEqual(self.stack.__len__(),4)

    def test_stacks(self):
        for i in range(35):

            self.setOfStack.push(i)
        lst = []
        for _ in range(35):
            import pdb; pdb.set_trace()
            lst.append(self.setOfStack.pop_at(0))
        self.assertEqual(lst,list(range((35))))






if __name__ == '__main__':
    unittest.main()
