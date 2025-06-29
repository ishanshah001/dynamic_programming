class Solution:
    def rob(self, nums):
        
        def help(nums):
            n = len(nums)
            if not nums:
                return 0
            if n==1:
                return nums[0]
            
            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2,n):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[-1]
        
        return max(nums[0],help(nums[1:]), help(nums[:-1]))
        