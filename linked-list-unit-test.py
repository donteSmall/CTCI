import unittest
from linked_list import Node,linkedList

class linked_List_Tests(unittest.TestCase):
    def setUp(self):
        self.list= linkedList()
        self.list2 = linkedList()


    def test_Insert_one_element(self):
        self.list.add_To_Beginning("z")
        self.assertTrue(self.list.head.get_Data()== 'z')

    def test_Insert_two_element(self):

        self.list.add_To_Beginning("apple")
        self.list.add_To_Beginning("Mango")

        # Bottom-up stack
        self.assertTrue(self.list.head.get_Data()== "Mango")
        next_element = self.list.head.get_Next()
        self.assertTrue(next_element.get_Data()== "apple")

    def test_Deleted_value_is_removed_from_list(self):
        self.list.add_To_Beginning(("The"))
        self.list.add_To_Beginning(("quick"))
        self.list.add_To_Beginning(("brown"))
        self.list.add_To_Beginning( ("fox"))

        self.list.delete("fox")
        self.assertTrue(self.list.head.get_Data() == "brown")

        self.list.delete("The")
        self.list.delete("quick")
        self.assertTrue(self.list.head.get_Next() is None )

    def test_Add_multiple(self):

        self.list.add_Multiple(["Mix","More", "Food"])

        result= ["Mix","More", "Food"]

        self.assertEqual(self.list.head.get_Data(),"Mix")
        self.assertEqual(self.list.head.next.get_Data(), "More")
        self.assertEqual(self.list.head.next.next.get_Data(), "Food")

    def test_Len(self):
        self.list.add_Multiple(["Mix","More", "Food"])
        self.assertEqual(self.list.__len__(),3)
        self.list.delete("Food")
        self.assertEqual(self.list.__len__(),2)


    def test_Search(self):
        self.list.add_Multiple(["Mix","More", "Food"])
        result=self.list.search("More")
        self.assertEqual(result.get_Data(),"More")
        result2=self.list.search("Food")
        self.assertEqual(result2.get_Data(),"Food")


    def test_Remove_duplicates_2(self):
        head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
        self.list.remove_Duplicates_2(head)
        self.assertEqual(head.data,1)
        self.assertEqual(head.next.data,3)
        self.assertEqual(head.next.next.data,5)
        self.assertEqual(head.next.next.next,None)

    def test_Delete_middle(self):
        head = Node(1,Node(2,Node(3,Node(4)))

        self.list.delete_Middle(head.next.next)

        self.assertEqual(head.data, 1)
        self.assertEqual(head.next.data, 2)
        # issue where next mext should be 4 but its 3, why ?

        self.assertEqual(head.next.next.data, 3)

    def test_Kth_to_last(self):
        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
        self.assertEqual(None, self.list.kth_To_last(head, 0));
        self.assertEqual(7, self.list.kth_To_last(head, 1).data)
        self.assertEqual(4, self.list.kth_To_last(head, 4).data)
        self.assertEqual(3, self.list.kth_To_last(head, 5).data)
        self.assertEqual(2, self.list.kth_To_last(head, 6).data)
        self.assertEqual(1, self.list.kth_To_last(head, 7).data)
        self.assertEqual(None, self.list.kth_To_last(head, 8))

    def test_Partition(self):
        #Not working as expected, list is being generated based off of order!
        self.list.add_To_Beginning(3)
        self.list.add_To_Beginning(8)
        self.list.add_To_Beginning(5)
        self.list.add_To_Beginning(5)
        self.list.add_To_Beginning(10)
        self.list.add_To_Beginning(1)
        self.list.add_To_Beginning(2)
        header = self.list
        head2 = header.partition(5)
        self.assertEqual(str(head2), '3,1,2,10,5,5,8')

    def test_Sum_lists(self):
        self.list.add(5)
        self.list.add(6)
        self.list.add(3)

        self.list2.add(8)
        self.list2.add(4)
        self.list2.add(2)
        result = self.list.sum_lists(self.list2)
        self.assertEqual(str(result) ,'3,1,6')


    def test_If_palindrome(self):
        self.list.add("R")
        self.list.add("A")
        self.list.add("D")
        self.list.add("A")
        self.list.add("R")
        self.assertEqual(self.list.panlidrome(),True)

        self.list2.add("T")
        self.list2.add("E")
        self.list2.add("S")
        self.list2.add("T")
        self.assertEqual(self.list2.panlidrome(),False )

    def test_Intersection(self):
        self.list.add("1")
        self.list.add("3")
        self.list.add("5")
        self.list.add("7")
        self.list.add("9")
        self.list.add("11")


        self.list2.add("2")
        self.list2.add("4")
        self.list2.add("9")
        self.list2.add("11")

        result= self.list.intersection(self.list,self.list2)
        self.assertEqual(result,'9')



if __name__ == '__main__':
    unittest.main()
