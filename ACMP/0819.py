a, b, c = map(int, input().split())
surface_area = 2*(a*b + b*c + c*a)
volume = a*b*c
print(surface_area, volume)

