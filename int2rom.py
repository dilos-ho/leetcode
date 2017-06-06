class Solution(object):
    def intToRoman(self, num):
        nums = ['I','V','X','L','C','D','M']
        strnum = str(num)
        strlen = len(strnum)
        strbuilder = []
        while (strlen > 0):
            if (int(strnum[0]) == 9):
                strbuilder.append(nums[(strlen-1)*2])
                strbuilder.append(nums[(strlen-1)*2+2])
            elif (int(strnum[0]) == 8):
                strbuilder.append(nums[(strlen-1)*2+1])
                strbuilder.append(nums[(strlen-1)*2])
                strbuilder.append(nums[(strlen-1)*2])
                strbuilder.append(nums[(strlen-1)*2])
            elif (int(strnum[0]) == 7):
                strbuilder.append(nums[(strlen-1)*2+1])
                strbuilder.append(nums[(strlen-1)*2])
                strbuilder.append(nums[(strlen-1)*2])
            elif (int(strnum[0]) == 6):
                strbuilder.append(nums[(strlen-1)*2+1])
                strbuilder.append(nums[(strlen-1)*2])
            elif (int(strnum[0]) == 5):
                strbuilder.append(nums[(strlen-1)*2+1])
            elif (int(strnum[0]) == 4):
                strbuilder.append(nums[(strlen-1)*2])
                strbuilder.append(nums[(strlen-1)*2+1])
            elif (int(strnum[0]) == 3):
                strbuilder.append(nums[(strlen-1)*2])
                strbuilder.append(nums[(strlen-1)*2])
                strbuilder.append(nums[(strlen-1)*2])
            elif (int(strnum[0]) == 2):
                strbuilder.append(nums[(strlen-1)*2])
                strbuilder.append(nums[(strlen-1)*2])
            elif (int(strnum[0]) == 1):
                strbuilder.append(nums[(strlen-1)*2])
            else:
                strbuilder.append('')
            strnum = strnum[1:]
            strlen -= 1
        return ''.join(strbuilder)
