class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # for every pair of i and j.. minimum length is - 2, including i adn j
        dp = [[2 for i in range(len(arr))] for j in range(len(arr))]
        ele_to_index = {ele:i for i, ele in enumerate(arr)}
        maxLength = 2
        for i in range(1, len(arr)):
            for j in range(0, i):
                previous_ele = arr[i] - arr[j]
                previous_ele_index = ele_to_index.get(previous_ele, None)
                if previous_ele_index is None or previous_ele_index>=j:
                    continue
                dp[i][j] = 1 + dp[j][previous_ele_index]
                maxLength = max(maxLength, dp[i][j])
        return maxLength if maxLength>2 else 0

