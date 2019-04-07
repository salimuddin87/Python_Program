"""
Count number of times a pattern appears in a given string as a subsequence
Input:
    String = "subsequence"
    Pattern = "sue"

Output: 7

1. su bs e quence
2. su bsequ e nce
3. su bsequenc e
4. s ubseq ue nce
5. s ubseq u enc e
6. sub s eq ue nce
7. subs eq u enc e
"""

def countSubsequence(S, P): 

    # P length can not be greater than S 
    if len(P) > len(S):
        print "P is greater than S!"
        return 0

    # String and Pattern has length 1 and contain same string
    if len(S) == 1 and P[0] == S[0]:
        print "P and S are equals with length 1!"
        return 1

    # when P becomes null
    if len(P) == 0:
        print "Length of P is 0 -> pattern found!"
        return 1
    # when S becomes null
    if len(S) == 0:
        print "Length of S is 0 -> Pattern not found!"
        return 0

    if S[0] == P[0]:
        print "First element matched in P and S!"
        print "countSubsequence(S[1:], P[1:]) + countSubsequence(S[1:], P)"
        return countSubsequence(S[1:], P[1:]) + countSubsequence(S[1:], P)
    else:
        print "No match in last comparison!"
        print "countSubsequence(S[1:], P)"
        return countSubsequence(S[1:], P)

if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    S = "subsequence"
    P = "sue"
    res = countSubsequence(S, P)
    print "Count of subsequence is : ", res
