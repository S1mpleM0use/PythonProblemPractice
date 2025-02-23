class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        counter_a = -1
        for i in nums:
            counter_a += 1
            counter_b = -1
            for j in nums:
                counter_b += 1
                if i == j and counter_a == counter_b:
                    continue
                if i + j == target:
                    return [counter_a, counter_b]

nms = [2,5,5,11]
trgt = 10
a = Solution()


print(a.twoSum(nms, trgt))