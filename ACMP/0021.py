worker1, worker2, worker3 = map(int, input().split())
salary = [worker1, worker2, worker3]
salary.sort()
print(salary[2] - salary[0])
