'''
Dynamic Problem

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right 
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there? 
Result will be the sum of paths
'''
#Big O
#Time O(mn)
#Space O (mn)

def uniquePaths(rows, columns):
    matrix =[[ 1 for j in range(rows)] for i in range(columns) ]

    for idx in range(1,columns):
        for jdx in range(1,rows):
            matrix[idx][jdx] = matrix[idx-1][jdx] + matrix[idx][jdx-1]
    return matrix[columns-1][rows-1]

import unittest
class Test(unittest.TestCase):
  def test_three_col_three_rows(self):
    self.assertEqual(uniquePaths(3,3), 6)

  def test_seven_col_three_rows(self):
    self.assertEqual(uniquePaths(7,3), 28)

  def test_(self):
    self.assertEqual(uniquePaths(7,5), 210)


if __name__ == "__main__":
  unittest.main()