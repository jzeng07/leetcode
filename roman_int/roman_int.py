#!/usr/bin/env python

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        num = 0
        roman_num_map = {
            "I": (0, 1),
            "V": (1, 5),
            "X": (2, 10),
            "L": (3, 50),
            "C": (4, 100),
            "D": (5, 500),
            "M": (6, 1000)
        }
        length = len(s)
        for i, v in enumerate(s):
            if i == len(s) - 1:
                num += roman_num_map[v][1]
                break
            if roman_num_map[v][0] < roman_num_map[s[i+1]][0]:
                num -= roman_num_map[v][1]
            else:
                num += roman_num_map[v][1]
        return num

roman_int = Solution()
print roman_int.romanToInt("IMMMM")     # 3999
print roman_int.romanToInt("XLVIII")    # 48
print roman_int.romanToInt("LXXXIV")    # 84
print roman_int.romanToInt("XCIII")     # 93
print roman_int.romanToInt("IV")        # 4

        
