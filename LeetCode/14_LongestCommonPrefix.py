#не додумался сам. посмотрел ответ
# смысл в том, чтобы проверять наличие подстроки в строке
# если ее нет, сокращаем подстроку на 1 элемент и проверяем дальше

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix

a = Solution()

print(a.longestCommonPrefix(["flower","flow","flight"]))


#GPT-4o
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

# Example usage:
strs1 = ["flower", "flow", "flight"]
print(longest_common_prefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(longest_common_prefix(strs2))  # Output: ""

