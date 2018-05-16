'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        row = [1]
        rList = [row]
        for i in range(1,numRows):
            row = [x+y for x,y in zip([0]+row,row+[0])]
            rList.append(row)
        return rList