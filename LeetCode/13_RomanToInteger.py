class Solution:
    def romanToInt(self, s: str) -> int:
        regular_roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        combo_roman = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        false_roman = {
            'VI': -1,
            'XI': -1,
            'LX': -1,
            'CX': -1,
            'DC': -1,
            'MC': -1
        }

        result_list = []

        # # логика для отличающихся чисел
        # for i in range(len(s)-1):
        #     combo = s[i] + s[i+1]
        #     if combo in combo_roman.keys():
        #         result_list.append(combo_roman.get(combo))
        #
        #
        # #логика для обычных чисел
        #     if combo in false_roman.keys():
        #         result_list.append(regular_roman.get(s[i]))
        #
        #     #result_list.append(regular_roman.get(s[i]))



        return sum(result_list)





a = Solution()

print(a.romanToInt("MCMXCIV"))
