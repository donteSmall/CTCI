import unittest
from collections import Counter

def unique(string):
    lettersContainer = {}
    for letter in string:
        if letter in lettersContainer:
            return False
        lettersContainer[letter]= True
    return True

def Permutation(string1, string2):
    if len(string1)!= len(string2):
        return False
    counter = Counter()
    for letter in string1:
        counter[letter] +=1

    for letter in string2:
        if counter[letter]==0:
            return False
        counter[letter] -=1
    return True

def URLify(string, length):
    new_idx = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            #replace spaces
            string[new_idx - 3: new_idx] = '%20'
            new_idx-=3
        else:
            #Move characters
            string[new_idx- 1]= string[i]
            new_idx-=1
    return string

def palindrome_Permutation(str1):
    str1 = str1.replace(" ", "")
    str1= str1.lower()

    d = dict()
    for i in str1:
        if i in d:
            #increment value by 1
            d[i]+=1
        else:
            d[i]=1
    odd_count= 0
    for k,v in d.items():
        #V==oddValue & Equal to Zero
        if v % 2 != 0 and odd_count == 0:
            #increment counter by 1
            odd_count+=1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

def one_away(s1,s2):
    if len(s1) == len(s2):
        return one_edit_replace(s1,s2)
    elif len(s1) + 1 == len(s2):
        return one_insert_replace(s1,s2)
    elif len(s1)-1 == len(s2):
        return one_edit_insert(s2,s1)
    return False

def one_edit_replace(s1,s2):
    edited= False
    for c1,c2, in zip(s1,s2):
        if c1 !=c2:
            if edited:
                return False
            edited = True
    return True
def one_edit_insert(s1,s2):
    edited= False
    i,j = 0,0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
        return True

def string_compression(string):
    compr_str =""
    count= 1


    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count+=1
        else:
            compr_str += string[i] + str(count)
            count =1
 #indet out of the loop
    compr_str += string[i] + str(count)
    if len(compr_str) >= len(string):

        return string
    else:
        return compr_str


#def print_matrix(matrix):
    #print "\n".join([ " ".join(str(l)) for l in matrix])

def rotate_matrix(matrix):
    n = len(matrix)
    #print_matrix(matrix)
    print

    for layer in range(n//2):
        first,last = layer, n - layer -1
        for i in range(first,last):
            #print("layer: %s i: %s" % (layer, i))
            # save top
            top = matrix[layer][i]
            #left-> top
            matrix[layer][i] = matrix[-i -1][layer]
            #bottom -> left
            matrix[-i - 1][layer] = matrix[-layer -1][-i -1]
            #right -> bottom
            matrix[-layer -1][-i -1] = matrix[i][-layer - 1]
            #top -> right
            matrix[i][-layer-1] = top

            #print_matrix(matrix)
            print


    return matrix


def zerofy(mat):
    firstRowHasZeros= False
    firstColHasZeros= False

    #checks if first colums has any zeros
    for i in range(0,len(mat)):
        if mat[i][0]==0:
            firstColHasZeros= True
            break

    #checks if first row has any zeros
    for i in range(0,len(mat[0])):
        if mat[0][i]== 0:
            firstRowHasZeros= True
            break

    #check the rest of matrix for zeros,
    #mark the row and column using first row and column

    for i in range(1, len(mat)):
        for j_indx in range(1,len(mat[0])):
            if mat[i][j_indx]== 0:
                mat[0][j_indx] =0 # first row mark !
                mat[i][0] = 0  # first col mark !

    # Zerofy the marked colums and Rows.
    for i in range(0,len(mat)):
        if mat[i][0] == 0:
            for j_indx in range(1,len(mat[0])):
                mat[i][j_indx]=0

    for i in range(1,len(mat[0])):
        if mat[0][i] == 0:
            for j_indx in range(1,len(mat)): # why not use indexing here ?
                mat[j_indx][i] = 0

    # Zero first row then col, if necessary !!!!

    if firstRowHasZeros:
        for i in range(0,len(mat[0])):
            mat[0][i] = 0

    if firstColHasZeros:
        for i in range(0,len(mat)):
            mat[i][0] = 0


    return mat



def is_substring(s1,s2):
    return s1 in s2

def string_rotation(s1,s2):
    return is_substring(s2,s1+s1)





class string_Test(unittest.TestCase):
#O(N)
    test_1 = [('abcd'), ('s4fad'),('')]
    test_2 = [('23ds2'), ('hb 627jh=j ()')]

    def test_unqiue(self):
        #true check
        for test_string in self.test_1:
            actual = unique(test_string)
            self.assertTrue(actual)
        #false check
        for test_string in self.test_2:
            actual = unique(test_string )
            self.assertFalse(actual)
#----------------------------------------------------------------
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),)
    dataF = (('abcd', 'd2cba'),
             ('2354', '1234'),
             ('dcw4f', 'dcw5f'),)

    def test_Permutation(self):
        for test_string in self.dataT:
            result = Permutation(*test_string )
            self.assertTrue(result)

        for test_string in self.dataF:
            result = Permutation(*test_string )
            self.assertFalse(result)
#----------------------------------------------------------------


    URLify_test_data = [(list('much ado about nothing      '), 22,
                        list('much%20ado%20about%20nothing')),
                        (list('Mr John Smith    '),13,
                        list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length,expected] in self.URLify_test_data:
            actual = URLify(test_string, length)
            self.assertEqual(actual, expected)
#----------------------------------------------------------------

    palindrome_Permutation_test_dataNot = [('Tact Coa', True)]
    palindrome_Permutation_test_dataT = [('Was it a cat I saw?', True)]
    palindrome_Permutation_test_dataF = [('Not a Palindrome', False)]


    def test_palindrome_Permutation(self):
        for [test_string, expected] in self.palindrome_Permutation_test_dataNot:
            actual = palindrome_Permutation(test_string)
            self.assertEqual(actual,expected)

        for [test_string2, expected] in self.palindrome_Permutation_test_dataF:
            actual = palindrome_Permutation(test_string2)
            self.assertEqual(actual,expected)
#----------------------------------------------------------------
    one_away_test_data = [('pale', 'bake', False)]

    def test_one_away(self):

        for [test_str1,test_str2,expected] in self.one_away_test_data:

            actual = one_away(test_str1,test_str2)
            self.assertEqual(actual,expected)

#----------------------------------------------------------------
    string_compressiont = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')]

    def test_string_compression(self):
        for [test_string, expected] in self.string_compressiont:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


#----------------------------------------------------------------
    data =[
            ([
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]
            ], [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5]
            ])
        ]
    def test_rotate_matrix(self):
            for [test_matrix, expected] in self.data:
                actual = rotate_matrix(test_matrix)
                self.assertEqual(actual, expected)
#----------------------------------------------------------------
    data_zero_matrix =[
            ([
                [1,1,1,1],
                [0,1,1,1],
                [1,1,1,1]
            ], [
                [0,1,1,1],
                [0,0,0,0],
                [0,1,1,1]
            ])
        ]
    def test_zero_matrix(self):
            for [test_matrix, expected] in self.data_zero_matrix:
                actual = zerofy(test_matrix)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
