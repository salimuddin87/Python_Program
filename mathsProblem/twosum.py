class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        res = []
        i = 0
        while i < n:
            temp = target - nums[i]
            tList = nums[i+1:]
            if temp in tList:
                res.append(i)
                res.append(i + tList.index(temp) + 1)
                break
            i += 1
        return res