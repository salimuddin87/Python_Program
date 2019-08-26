

def printExcelColNo(A):
	T = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
	return sum(T[ch] * 26**i for i, ch in enumerate(A[::-1]))

if __name__ == '__main__':

    print(printExcelColNo('A'))