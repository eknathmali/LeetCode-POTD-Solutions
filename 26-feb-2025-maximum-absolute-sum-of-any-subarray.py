class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]] * len(nums)
        for i in range(1,len(nums)): prefix_sum[i] = prefix_sum[i-1] + nums[i]


        maxSum, maxi, mini = 0, 0, 0
        for i in range(len(nums)):
            maxSum = max(maxSum, abs(prefix_sum[i]-mini),abs(prefix_sum[i]-maxi))
            maxi = max(maxi, prefix_sum[i])
            mini = min(mini, prefix_sum[i])

        return maxSum
