
def hotel(arrive, depart, K):
	n = len(arrive)
	ans = []
	for i in range(n):
		ans.append((arrive[i], 1))
		ans.append((depart[i], 0))

	ans.sort()
	curr_active = max_active = 0
	for i in range(len(ans)):
		if ans[i][1] == 1:
			curr_active += 1
			max_active = max(max_active, curr_active)
		else:
			curr_active -= 1

	return K >= max_active

if __name__ == '__main__':
    print hotel([1,3,5], [2,6,8], 1)

"""
class Solution:
    def hotel(self, arrive, depart, K):
        events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
        events = sorted(events)

        guests = 0

        for event in events:
            if event[1] == 1:
                guests += 1
            else:
                guests -= 1

            if guests > K:
                return 0

        return 1

"""    