from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to group duplicates together

        def backtrack(start: int, path: List[int]):
            res.append(path[:])  # Add current subset

            for i in range(start, len(nums)):
                # Skip duplicates at the same recursion depth
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1, 2, 1]
    print("Input:", nums1)
    print("Output:", solution.subsetsWithDup(nums1))
    
    nums2 = [7, 7]
    print("\nInput:", nums2)
    print("Output:", solution.subsetsWithDup(nums2))
