class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """

            1. Use prefix sum
            2. to get odd count subarray at any index j
                number of opposite parity (prefix sum till j-1)
        """
        prefix_sum = [arr[0]] * len(arr)
        for i in range(1, len(arr)):
                prefix_sum[i] = prefix_sum[i-1] + arr[i]
            
        even, odd = 1, 0
        result = 0
        mod = 1e9+7
        for i in range(len(prefix_sum)):
            if prefix_sum[i]%2==0:
                result = (result+odd) % mod
                even += 1
            else:
                result = (result + even) % mod
                odd +=1
            
        return int(result)