'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

Example:
Input: 3
Output: [1,3,3,1]
'''
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        arr = [1]
        for i in range(rowIndex):
            arr = [x+y for x,y in zip([0]+arr,arr+[0])]
        return arr