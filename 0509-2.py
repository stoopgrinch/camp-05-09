N = list(map(int, input().split()))
a = [input().split() for l in range(N[1])]

T = [[] for i in range(N[0])]

for j in range(N[0]):
    for i in range(N[1]):
        T[j].append(a[i][j])

for i in range(len(T)):
    T[i] = list(map(int, T[i]))

x = []

for i in range(len(T)):
    x.append(T[i].index(max(T[i])))

x = sorted(x)
max = 0

for n in x:
    num = x.count(n)
    if num > max:
        max = num
        md = n

print(md + 1, x.count(md))
