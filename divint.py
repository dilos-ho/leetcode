class Solution(object):
    def divide(self, dividend, divisor):
        neg = None
        result = []
        digits = []
        i = 0
        if (dividend < 0 and divisor < 0):
            neg = False
            dividend = abs(dividend)
            divisor = abs(divisor)
        elif (dividend < 0 and divisor > 0):
            neg = True
            dividend = abs(dividend)
        elif (dividend > 0 and divisor < 0):
            neg = True
            divisor = abs(divisor)
        else:
            neg = False
        strnum = str(dividend)
        while (i < len(strnum)):
            count = 0
            digits.append(strnum[i])
            currval = ''.join(digits)
            intform = int(currval)
            if (intform < divisor):
                result.append(str(0))
                i += 1
            else:
                while (divisor <= intform):
                    intform -= divisor
                    count += 1
                digits = list(str(intform))
                result.append(str(count))
                i += 1
        relval = int(''.join(result))
        if (neg):
            relval = -relval
        if ((relval > 2147483647) or (relval < -2147483648)):
            return 2147483647
        return relval
        
a = Solution()
print (a.divide(-2147483648,1));



