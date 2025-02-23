#посмотрел в ответ
M, N = map(int, input().split())

R1 = M*N-1

R2 = N*(M-1)+M*(N-1)

print(R2-R1)