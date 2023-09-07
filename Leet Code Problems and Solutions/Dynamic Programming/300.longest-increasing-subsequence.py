#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        tmp = [nums[0]]

        for n in nums:
            x = bisect_left(tmp,n)

            if x == len(tmp):
                tmp.append(n)
            elif tmp[x]>n:
                tmp[x]=n
        return len(tmp)

        
        
        # N = len(nums)
        # dp = [N]*1

        # for n in range(N):
        #     for i in range(n):
        #         if nums[i]<nums[n]:
        #             dp[n]= max(dp[n],dp[i]+1)
        # return max(dp)
        
# @lc code=end

