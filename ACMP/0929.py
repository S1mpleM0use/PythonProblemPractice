points = int(input())

dictionary = {
    1: 6,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1
}


maximum = points * 6
minimum = 0


sixes = points // 6
dic_key = points - 6 * sixes
minimum = sixes
if dic_key > 0:
    minimum = sixes + dictionary.get(dic_key)



print(minimum, maximum)