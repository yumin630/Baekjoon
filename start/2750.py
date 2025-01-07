N = int(input())
a = []

for i in range(N):
    num = int(input())
    a.append(num)

a.sort()
for i in a:
    print(i)