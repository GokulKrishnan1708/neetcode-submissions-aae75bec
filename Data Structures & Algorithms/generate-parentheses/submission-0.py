class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(openN, closeN, cur):
            if openN == closeN == n:
                res.append(cur)
                return
            if openN < n:
                backtrack(openN + 1, closeN, cur + "(")
            if closeN < openN:
                backtrack(openN, closeN + 1, cur + ")")
        
        backtrack(0, 0, "")
        return res