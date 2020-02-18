# Find max substring from a given string without repeatation

def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if not s:
    	return n
    hashSet = s[0]
    i = 0
    j = 1
    maxL = 1
    while i < n and j < n:
    	print(i, j, maxL, hashSet)
    	if s[j] not in hashSet:
    		hashSet += s[j]
    		if maxL < (j - i + 1):
    			maxL = j - i + 1
    		j += 1
    	else:
    		while i < j and s[i] != s[j]:
    			i += 1
    		hashSet = s[i+1:j+1]
    		j += 1
    		i += 1
        
    return maxL


if __name__ == '__main__':
	#import pdb; pdb.set_trace()
	print(lengthOfLongestSubstring("abcabcbb"))
	print("#" * 20)
	print(lengthOfLongestSubstring("abcabcbbabcd"))