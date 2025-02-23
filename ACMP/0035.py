k = int(input())
final_list = []
for i in range(1, k+1):
    n, m = map(int, input().split())
    d = 19*m + (n + 239) * (n + 366) / 2
    final_list.append(int(d))

for i in final_list:
    print(i)
