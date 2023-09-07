class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N =  len(nums)
        dp = [1] * N
        
        for n in range(N):
            for i in range(n):
                if nums[i]<nums[n]:
                    dp[n]=max(dp[n],dp[i]+1)
        return max(dp)