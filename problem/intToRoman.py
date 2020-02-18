from collections import OrderedDict
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = OrderedDict()
        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"
        
        res = ""
        for r in roman.keys():
            x, y = divmod(num, r)
            res += roman[r] * x
            num -= (r * x)
            if num <= 0:
                break
        
        return res