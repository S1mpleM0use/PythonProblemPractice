c, h, o = map(int, input().split())

answer = [c//2, h//6, o//1]
answer.sort()

print(answer[0])