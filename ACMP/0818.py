triplers = int(input())
info = list(map(int, input().split()))
real_info = info[:triplers]

result = 0
for i in real_info:
    result += i

result += 1
print(result - triplers)