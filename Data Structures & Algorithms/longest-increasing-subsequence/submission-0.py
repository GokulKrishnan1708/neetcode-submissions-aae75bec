class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        import bisect
        for n in nums:
            i = bisect.bisect_left(dp, n)
            if i == len(dp):
                dp.append(n)
            else:
                dp[i] = n
        return len(dp)