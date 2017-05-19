class Solution(object):
    def reverse(self, x):
        maxnum = 2147483647                 #grabbed this value from googling
        strform = str(x)
        if (x < 0):
            strform = strform[1:]
        revform = strform[::-1]
        if (int(revform) > maxnum):
            return 0
        else:
            if (x < 0):
                return (0 - int(revform))
            else:
                return int(revform)
