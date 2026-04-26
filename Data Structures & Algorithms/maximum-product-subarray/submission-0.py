class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = nums[0], nums[0]

        for n in nums[1:]:
            tmp = curMax
            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, n * tmp, n * curMin)
            res = max(res, curMax)

        return res