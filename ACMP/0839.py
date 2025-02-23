response = input()
check = 0
for i in response:
    if int(i) == 0:
        check = 1
        print('NO')
        break
if check == 0:
    print('YES')