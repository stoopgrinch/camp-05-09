N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

x = ""

for i in range(N):
        x += str(A[i] - B[i]) 
        x += " "

print(x)
