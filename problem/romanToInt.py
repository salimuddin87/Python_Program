from collections import OrderedDict
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = OrderedDict()
        roman["M"] = 1000
        roman["CM"] = 900
        roman["D"] = 500
        roman["CD"] = 400
        roman["C"] = 100
        roman["XC"] = 90
        roman["L"] = 50
        roman["XL"] = 40
        roman["X"] = 10
        roman["IX"] = 9
        roman["V"] = 5
        roman["IV"] = 4
        roman["I"] = 1
        
        res = 0
        for key in roman.keys():
            l = len(key)
            while key == s[:l]:
                res += roman[key]
                s = s[l:]
        return res