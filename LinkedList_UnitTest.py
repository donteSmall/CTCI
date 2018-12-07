import unittest
from LinkedList_V2 import Node,linkedList

class linked_List_Tests(unittest.TestCase):
    def setUp(self):
        self.list= linkedList()


    def test_insert_one_element(self):
        self.list.add_to_beginning("z")
        self.assertTrue(self.list.head.get_data()== 'z')

    def test_insert_two_element(self):

        self.list.add_to_beginning("apple")
        self.list.add_to_beginning("Mango")

        # Bottom-up stack
        self.assertTrue(self.list.head.get_data()== "Mango")
        next_element = self.list.head.get_next()
        self.assertTrue(next_element.get_data()== "apple")

    def test_deleted_value_is_removed_from_list(self):
        self.list.add_to_beginning("The")
        self.list.add_to_beginning("quick")
        self.list.add_to_beginning("brown")
        self.list.add_to_beginning("fox")

        self.list.delete("fox")
        self.assertTrue(self.list.head.get_data() == "brown")

        self.list.delete("The")
        self.list.delete("quick")
        self.assertTrue(self.list.head.get_next() is None )

    def test_add_multiple(self):

        self.list.add_multiple(["Mix","More", "Food"])

        result= ["Mix","More", "Food"]

        self.assertEqual(self.list.head.get_data(),"Mix")
        self.assertEqual(self.list.head.next.get_data(), "More")
        self.assertEqual(self.list.head.next.next.get_data(), "Food")

    def test_len(self):
        self.list.add_multiple(["Mix","More", "Food"])
        self.assertEqual(self.list.__len__(),3)
        self.list.delete("Food")
        self.assertEqual(self.list.__len__(),2)


    def test_search(self):
        self.list.add_multiple(["Mix","More", "Food"])
        result=self.list.search("More")
        self.assertEqual(result.get_data(),"More")
        result2=self.list.search("Food")
        self.assertEqual(result2.get_data(),"Food")

    def test_remove_duplicates(self):
        self.list.add_to_beginning("a")
        self.list.add_to_beginning("a")
        self.list.add_to_beginning("b")
        self.list.add_to_beginning("c")
        self.list.add_to_beginning("c")
        self.list.add_to_beginning("c")
        self.list.add_to_beginning("d")
        self.list.add_to_beginning("e")
        self.list.add_to_beginning("e")
        import pdb; pdb.set_trace()
        result = self.list.remove_duplicates()
        self.assertEqual(result, ['a','b','c','d','e'])











if __name__ == '__main__':
    unittest.main()
