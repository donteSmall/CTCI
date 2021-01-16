import unittest
from collections import Counter
 
class ArrayNString:

    def unique(self,string):
        lettersContainer = {}
        for letter in string:
            if letter in lettersContainer:
                return False
            lettersContainer[letter]= True
        return True


    def check_Permutation(self,string1, string2):

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

    def URLify(self,string, length):
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

    def palindrome_Permutation(self, str1):
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


    def one_away(self,s1,s2):
        if len(s1) == len(s2):
            return self.one_edit_replace(s1,s2)
        elif len(s1) + 1 == len(s2):
            return self.one_edit_insert(s1,s2)
        elif len(s1)-1 == len(s2):
            return self.one_edit_insert(s2,s1)
        return False

    # No Test
    def one_edit_replace(self,s1,s2):
        edited= False
        for c1,c2, in zip(s1,s2):
            if c1 !=c2:
                if edited:
                    return False
                edited = True
        return True
        
    # No Test
    def one_edit_insert(self,s1,s2):
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

    def string_compression(self, string):
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

    def rotate_matrix(self, matrix):
        n = len(matrix)
        #print_matrix(matrix)

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
            
        return matrix


    def zerofy(self,mat):
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


# No Test
def is_substring(s1,s2):
    return s1 in s2
# No Test
def string_rotation(s1,s2):
    return is_substring(s2,s1+s1)

