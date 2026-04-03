class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start):
            if start == len(s):
                res.append(part[:])
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    part.append(s[start:end+1])
                    dfs(end + 1)
                    part.pop()

        dfs(0)
        return res