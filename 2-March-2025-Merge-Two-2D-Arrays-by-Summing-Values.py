class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """
        2-March-2025-Merge-Two-2D-Arrays-by-Summing-Values.py
        """
        result = []
        i, j = 0,0
        while i<len(nums1) and j<len(nums2):
            id1, val1 = nums1[i][0], nums1[i][1]
            id2, val2 = nums2[j][0], nums2[j][1]

            if id1== id2:
                result.append([id1, val1+val2])
                j+=1
                i +=1
            elif id1<id2:
                result.append([id1, val1])
                i +=1
            else:
                result.append([id2, val2])
                j +=1
        
        while i< len(nums1):
            id1, val1 = nums1[i][0], nums1[i][1]
            result.append([id1, val1])
            i +=1
        
        while j< len(nums2):
            id2, val2 = nums2[j][0], nums2[j][1]
            result.append([id2, val2])
            j +=1
        
        return result

