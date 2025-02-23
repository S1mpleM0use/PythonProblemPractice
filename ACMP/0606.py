a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')

# # ответ:
# X, Y, Z = map(int, input().split())
# if max(X, Y, Z) < X + Y + Z - max(X, Y, Z):
#     print('YES')
# else:
#     print('NO')