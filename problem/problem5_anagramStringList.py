"""
let the input S = ['code','aaangrms','anagrams','doce','aaangrmss']
then the output is "aaangrms, code"

"""

class Anagram:

    def findAnagram(self, S):
        res = []
        for i in range(0, len(S)):
            str1 = S[i]
            for j in range(i+1, len(S)):
                if S[j] == '0':
                    continue
                str2 = S[j]

                # Proceed if both str have same length
                if len(str1) != len(str2):
                    continue

                # Convert str to list and sort them
                str1List = list(str1)
                str2List = list(str2)

                str1List.sort()
                str2List.sort()

                if cmp(str1List, str2List) == 0:
                    S[j] = '0'
                    res.append(str1)
        out = list(set(res))
        out.sort()
        return out

if __name__ == '__main__':

    obj = Anagram()
    S = ['code','aaangrms','anagrams','doce','aaangsrm']
    res = obj.findAnagram(S)
    print res
