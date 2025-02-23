list_res_one = []
list_res_two = []
counter1 = 0
counter2 = 0

for i in range(4):
    a, b = map(int, input().split())
    list_res_one.append(a)
    list_res_two.append(b)

for i in list_res_one:
    counter1 += i

for j in list_res_two:
    counter2 += j

if counter1 > counter2:
    print(1)
if counter2 > counter1:
    print(2)
if counter1 == counter2:
    print('DRAW')
