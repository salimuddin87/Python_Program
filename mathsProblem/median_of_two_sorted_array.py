# Median to two sorted array
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nA = len(nums1)
        nB = len(nums2)
        
        if not nA and nB == 1:
            return nums2[0]
        if not nB and nA == 1:
            return nums1[0]
        if nA ==1 and nB == 1:
            return (nums1[0] + nums2[0])/2
        
        tl = nA + nB
        medIndex = 0
        even = False
        
        if tl % 2 == 0:
            medIndex = int(tl / 2 - 1)
            even = True
        else:
            medIndex = int((tl - 1)/2)
        
        i = j = count = 0
        while i < nA and j < nB:
            if nums1[i] < nums2[j]:
                if count == medIndex:
                    if even:
                        if (i+1) < nA:
                            return (nums1[i] + min(nums1[i+1], nums2[j]))/2
                        else:
                            return (nums1[i] + nums2[j])/2
                    return nums1[i]
                i += 1
            else:
                if count == medIndex:
                    if even:
                        if (j+1) < nB:
                            return (nums2[j] + min(nums2[j+1], nums1[i]))/2
                        else:
                            return (nums2[j] + nums1[i])/2
                    return nums2[j]
                j += 1
            count += 1
        while i < nA:
            if count == medIndex:
                if even:
                    return (nums1[i] + nums1[i+1])/2
                return nums1[i]
            i += 1
            count += 1
        while j < nB:
            if count == medIndex:
                if even:
                    return (nums2[j] + nums2[j+1])/2
                return nums2[j]
            j += 1
            count += 1
