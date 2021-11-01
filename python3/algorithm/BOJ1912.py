N = int(input())
L = list(map(int, input().split()))
S = 0
D = max(L)

for i in range(N):
	if L[i] + S >= 0:
		S += L[i]
		D = max(D, S)
	else:
		S = 0
print(D)
