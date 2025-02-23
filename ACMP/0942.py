tasks = int(input())
minutes = list(map(int, input().split()))

summa = 0
stud_5 = 0
for a in minutes:
    summa += a
    stud_5 += 1
    if summa > 300:
        summa -= a
        stud_5 -= 1
        break

summa = 0
stud_3 = 0
for a in minutes[::-1]:
    summa += a
    stud_3 += 1
    if summa > 300:
        summa -= a
        stud_3 -= 1
        break

summa = 0
stud_1 = 0
minutes.sort()
for a in minutes:
    summa += a
    stud_1 += 1
    if summa > 300:
        summa -= a
        stud_1 -= 1
        break

if stud_5 > stud_3 and stud_5 > stud_1:
    print(5)
elif stud_3 > stud_1:
    print(3)
else:
    print(1)
