class Solution(object):
    def romanToInt(self, s):
        #going to define a dictionary for these numbers first
        rom_dict = {}
        rom_dict['I'] = 1
        rom_dict['V'] = 5
        rom_dict['X'] = 10
        rom_dict['L'] = 50
        rom_dict['C'] = 100
        rom_dict['D'] = 500
        rom_dict['M'] = 1000
        #finished defining dictionary for integers 1-3999
        val = 0
        i = 0
        while (i < len(s)):
            if (i+1 < len(s)):
                if (rom_dict[s[i]] < rom_dict[s[i+1]]):
                    temp = rom_dict[s[i+1]] - rom_dict[s[i]]
                    val += temp
                    i += 2
                else:
                    val += rom_dict[s[i]]
                    i += 1
            else:
                val += rom_dict[s[i]]
                i += 1
        return val
