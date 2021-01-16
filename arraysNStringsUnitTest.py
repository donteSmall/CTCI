import unittest
from arraysNStrings import ArrayNString

class arrays_and_strings_tests(unittest.TestCase):
    
    def setUp(self):
        self.arraysNStrings  = ArrayNString()

    
    def test_unqiue(self):
        # Assume
        test_1 = [('abcd'), ('s4fad'),('')]
        test_2 = [('23ds2'), ('hb 627jh=j ()')]

        # Action
        for test_string in test_1:
            actual = self.arraysNStrings.unique(test_string)
        # Assert
            self.assertTrue(actual)
        
        for test_string in test_2:
            actual = self.arraysNStrings.unique(test_string )
        # Assert
            self.assertFalse(actual)
   

    def test_Permutation(self):
        # Assume
        dataT = (('abcd', 'bacd'),('3563476', '7334566'),('wef34f', 'wffe34'),)
        dataF = (('abcd', 'd2cba'),('2354', '1234'),('dcw4f', 'dcw5f'),)

        # Action
        for test_string in dataT:
            
            result = self.arraysNStrings.check_Permutation(*test_string)
        # Assert
            self.assertTrue(result)

        for test_string in dataF:
            result = self.arraysNStrings.check_Permutation(*test_string )
            self.assertFalse(result)
    

    def test_urlify(self):
        # Assume
        URLify_test_data = [(list('much ado about nothing      '), 22,
                        list('much%20ado%20about%20nothing')),
                        (list('Mr John Smith    '),13,
                        list('Mr%20John%20Smith'))]
         # Action
        for [test_string, length,expected] in URLify_test_data:
            actual = self.arraysNStrings.URLify(test_string, length)

            # Assert
            self.assertEqual(actual, expected)

   


    def test_palindrome_Permutation(self):
        palindrome_Permutation_test_dataNot = [('Tact Coa', True)]
        palindrome_Permutation_test_dataT = [('Was it a cat I saw?', True)]
        palindrome_Permutation_test_dataF = [('Not a Palindrome', False)]

        for [test_string, expected] in palindrome_Permutation_test_dataNot:
            actual = self.arraysNStrings.palindrome_Permutation(test_string)
            self.assertEqual(actual,expected)

        for [test_string2, expected] in palindrome_Permutation_test_dataF:
            actual = self.arraysNStrings.palindrome_Permutation(test_string2)
            self.assertEqual(actual,expected)
    
    

    def test_one_away(self):
        one_away_test_data = [('pale', 'bake', False)]

        for [test_str1,test_str2,expected] in one_away_test_data:

            actual = self.arraysNStrings.one_away(test_str1,test_str2)
            self.assertEqual(actual,expected)
        

    def test_string_compression(self):
        string_compressiont = [('aabcccccaaa', 'a2b1c5a3'), ('abcdef', 'abcdef')]

        for [test_string, expected] in string_compressiont:
            actual = self.arraysNStrings.string_compression(test_string)
            self.assertEqual(actual, expected)
    
        
    def test_rotate_matrix(self):

        data = [([ [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]], 
                [[21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5]])]

        for [test_matrix, expected] in data:
            actual = self.arraysNStrings.rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

       
    def test_zero_matrix(self):

        data_zero_matrix =[
            ([
                [1,1,1,1],
                [0,1,1,1],
                [1,1,1,1]
            ], [
                [0,1,1,1],
                [0,0,0,0],
                [0,1,1,1]
            ])]
        for [test_matrix, expected] in data_zero_matrix:
            actual = self.arraysNStrings.zerofy(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()