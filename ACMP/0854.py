room_t, goal_t = map(int, input().split())
mode = input()

if mode == 'freeze':
    if goal_t >= room_t:
        print(room_t)
    if goal_t < room_t:
        print(goal_t)

if mode == 'heat':
    if goal_t >= room_t:
        print(goal_t)
    if goal_t < room_t:
        print(room_t)

if mode == 'auto':
    print(goal_t)

if mode == 'fan':
    print(room_t)