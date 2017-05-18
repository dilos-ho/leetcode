class Solution(object):
    def lengthOfLongestSubstring(self, s):
        x = 0
        substrs = []
        tempstr = []
        while (x < len(s)): 
            if (s[x] in tempstr):
                substrs.append("".join(tempstr))
                while (tempstr[0] != s[x]):
                    tempstr.remove(tempstr[0])
                tempstr.remove(tempstr[0])
            tempstr.append(s[x])
            x += 1            
        substrs.append("".join(tempstr))
        size = 0
        for k in range(len(substrs)):
            if (len(substrs[k]) > size):
                size = len(substrs[k])
        return size
