class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""
        for c in s:
            if c.isdigit():
                current_num = current_num * 10 + int(c)
            elif c == "[":
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif c == "]":
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += c
        return current_str