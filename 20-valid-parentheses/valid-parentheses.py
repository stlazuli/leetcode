class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        mapping = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in mapping.values():
                ans.append(char)
            elif char in mapping.keys():
                if not ans or mapping[char] != ans.pop():
                    return False
        
        return not ans
        