class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
         dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = 0
        for char in s:
            num = dict[char]
            result += num
            if num > prev:
                result -= 2 * prev
            prev = num
        return result
