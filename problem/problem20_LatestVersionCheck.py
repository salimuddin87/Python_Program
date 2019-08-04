import os

from collections import OrderedDict

presentDir = os.path.abspath(os.path.dirname(__file__))


def allLatestVersionApp(file):
	
	apiVersion = list()
	appDict = OrderedDict() # columns of apiVersion
	apiDict = OrderedDict() # rows of apiVersion
	appCount = 0
	apiCount = 0
	appChange = False
	apiChange = False

	with open(file, 'r') as fp:
		line = fp.readline()
		while line != "":
			#print(line)
			tempList = line.strip().split(',') # strip to remove newline

			# Add app if not present in appDict
			if tempList[0].strip() not in appDict.keys():
				appDict[tempList[0].strip()] = appCount
				appCount += 1
				appChange = True

			# Add api if not present in apiDict
			if tempList[1].strip() not in apiDict.keys():
				apiDict[tempList[1].strip()] = apiCount
				apiCount += 1
				apiChange = True

			# when new api comes create a new list
			if apiChange:
				apiVersion.append(["0" for x in range(appCount)])
				apiChange = False

			if appChange:
				# when new app comes append at the end
				apiVersion[apiDict[tempList[1].strip()]].append(tempList[2].strip())
				appChange = False
			else:
				# If api and app both exist
				row = apiDict[tempList[1].strip()]
				col = appDict[tempList[0].strip()]
				try:
					apiVersion[row][col] = tempList[2].strip()
				except IndexError as ie:
					# append when index is out of range
					apiVersion[row].append(tempList[2].strip())

			line = fp.readline()

	# check app whose all api is latest
	for colkey in appDict.keys():
		for rowkey in apiDict.keys():
			#print(rowkey, colkey)
			if apiVersion[apiDict[rowkey]][appDict[colkey]] == "0":
				if apiDict[rowkey] == len(apiVersion)-1:
					return colkey
				else:
					continue

			if apiVersion[apiDict[rowkey]][appDict[colkey]] != max(apiVersion[apiDict[rowkey]]):
				break
			
	return False

	"""
	output = presentDir + "/output.txt"
	with open(output, 'w') as fp:
		fp.write(str(appDict)+"\n")
		fp.write(str(apiDict)+"\n")
		for i in range(len(apiVersion)):
			fp.write(str(apiVersion[i])+"\n")

	return False
	"""

if __name__ == '__main__':
	file = presentDir + "/input.txt"
	#print(file)
	print(allLatestVersionApp(file))