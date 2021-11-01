#합

N = int(input())
ret = [0 for _ in range(N+1)]

for i in range(1, N+1):
	if i == 1:
		ret[i] = 1
	else:
		ret[i] = ret[i-1] + i

print(ret[N])
