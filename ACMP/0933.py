a, b, c, t = map(int, input().split())

if a >= t:
    print(t*b)
if a < t:
    print(a*b + (t-a) * c)