
def matchRegExp(s, p):
	n = len(s)
	m = len(p)

	i = j = 0
	while i < n and j < m:
		if p[j].isalpha():
			if s[i] == p[j]:
				i += 1
				j += 1
			else:
				if j < m-1 and p[j+1] == "*":
					j += 1
				else:
					return False
		elif p[j] == "*":
			if p[j-1] == ".":
				return True
			if p[j-1] == s[i]:
				i += 1
			elif j < m-1 and p[j-1] != s[i]:
			    j += 1 
			else:
				return False
		else:
			i += 1
			j += 1
	if i == n:
		while j < m and i == n:
			if p[j] == ".":
				return False
			elif p[j] == "*":
				j += 1
			elif p[j].isalpha() and j == m-1:
				return False
			elif p[j].isalpha() and p[j+1] == "*":
				j += 1
			else:
				return False

	if j == m and i < n:
		return False
	elif i == n and j == m-1 and p[j] == '*':
		return True
	elif i == n and j == m:
		return True
	else:
		return False

if __name__ == '__main__':
	#print(matchRegExp("aa", "a"))
	#print(matchRegExp("aa", "a*"))
	#print(matchRegExp("ab", ".*"))
	print(matchRegExp("aab", "c*a*bc*"))
	print(matchRegExp("mississippi", "mis*is*p*."))
	print(matchRegExp("abcd","d*"))
