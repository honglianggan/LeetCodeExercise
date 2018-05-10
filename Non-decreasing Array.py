'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element. 
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n). 
Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000]. 

'''
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        max = sys.maxsize
        min = -max
        nums = [min] + nums +[max]
        flag = True
        for i in range(2,len(nums)-1):
            if nums[i] -nums[i-1] <0:
                if flag:
                    if nums[i+1] - nums[i-1] >=0:flag=False
                    elif nums[i] - nums[i-2] >=0:flag=False
                    else:return False
                else:
                    return flag
        return True