class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            if '()' in s:
                s = s.replace('()', '', 1)
            if '[]' in s:
                s = s.replace('[]', '', 1)
            if '{}' in s:
                s = s.replace('{}', '', 1)

        if s:
            return False
        else:
            return True








s = Solution()

print(s.isValid('([])'))