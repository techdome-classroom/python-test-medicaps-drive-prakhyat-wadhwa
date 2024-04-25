class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = []
        dict = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in dict:
                top_element = check.pop() if check else '#'
                if dict[char] != top_element:
                    return False
            else:
                check.append(char)
        return not check
    



  

