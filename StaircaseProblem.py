

#Burte Force  implenmtation
def triple_steps(steps):

    if (steps == 0  or steps == 1):
        return 1

    if (steps == 2): 
        return 2

    return triple_steps(steps- 1) + triple_steps(steps - 2 ) + triple_steps( steps - 3 )

import unittest
class Test(unittest.TestCase):
  def test_triple_step(self):
    self.assertEqual(triple_steps(3), 4)
    self.assertEqual(triple_steps(7), 44)

if __name__ == "__main__":
  unittest.main()