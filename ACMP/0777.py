s, t = map(int, input().split())
if s == t:
    print('wha')
if t > 12:
    raise Exception("Inventin' new clocks, huh?")
if s < 1:
    raise Exception("bruh")
if t - s > 0:
    print(t - s)
if t - s < 0:
    print((12-s) + t)