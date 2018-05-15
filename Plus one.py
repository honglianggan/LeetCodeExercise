'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_list = [str(i) for i in digits]
        digits_str = "".join(digits_list)
        digits_int = int(digits_str)
        digits_int += 1
        digits_str = str(digits_int)
        digits = [int(i) for i in digits_str]
        return digits
		
class Solution2:
    def plusOne(self, digits):
		return list(map(int, list(str(int("".join(map(str, digits))) + 1))))