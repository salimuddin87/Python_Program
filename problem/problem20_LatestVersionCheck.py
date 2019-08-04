import os

presentDir = os.path.abspath(os.path.dirname(__file__))


def allLatestVersionApp(file):
	
	apiVersion = list()
	appDict = dict() # columns of apiVersion
	apiDict = dict() # rows of apiVersion
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
				apiVersion[apiCount-1][appCount-1] = tempList[2].strip()
				apiChange = False
			elif appChange:
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

	print(appDict)
	print(apiDict)
	for i in range(len(apiVersion)):
		print(apiVersion[i])
	return False

if __name__ == '__main__':
	file = presentDir + "/input.txt"
	print(file)
	print(allLatestVersionApp(file))