class Solution(object):
    def isPalindrome(self, x):
        strform = str(x)
        start = 0
        end = len(strform) - 1
        while (start < end):
            if (strform[start] != strform[end]):
                return False
            else:
                start += 1
                end -= 1
        return True
