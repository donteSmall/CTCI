import unittest

def sort_stack(stack):
  # temporary stack
  temp = Stack()

  previous_val = stack.pop()

  #curr holds value popped from end of stack
  current_val = stack.pop()

  # While stack has another item
  while current_val:
    #if current_val is less than
    #the last element in temp, append curr to temp
    if current_val < previous_val :
      temp.push(current_val)
    else:
      temp.push(previous_val)
      previous_val = current_val

    current_val = stack.pop()


  is_sorted = True
  current_val = temp.pop()
  while current_val:
      #if curr is greater than last element in temp
      #pop off last element and append element back to "stack"

    if current_val > previous_val:
      is_sorted = False
      stack.push(current_val)
    else:
      stack.push(previous_val)
      previous_val = current_val
    current_val = temp.pop()
#append temp to stack to flip in ascending order
  stack.push(previous_val)

  if is_sorted:
    return stack

  return sort_stack(stack)

class Stack():
  def __init__(self):
    self.top = None

  def __str__(self):
    return str(self.top)

  def push(self, item):
    self.top = current_val(item, self.top)

  def pop(self):
    if not self.top:
      return None

    item = self.top
    self.top = self.top.next

    return item.data

class current_val():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next

  def __str__(self):
    return str(self and self.data) + ',' + str(self and self.next)





class Test(unittest.TestCase):
    def test_sort_stack(self):
        stack = Stack()
        stack.push(10)
        stack.push(30)
        stack.push(70)
        stack.push(40)
        stack.push(80)
        stack.push(20)
        stack.push(90)
        stack.push(50)
        stack.push(60)
        self.assertEqual(str(stack), "60,50,90,20,80,40,70,30,10,None")
        self.assertEqual(str(sort_stack(stack)), "10,20,30,40,50,60,70,80,90,None")


if __name__ == "__main__":
  unittest.main()
