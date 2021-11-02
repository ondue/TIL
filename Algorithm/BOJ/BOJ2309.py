#TODO: 일곱 난쟁이

n = []
for i in range(9):
	a = int(input())
	n.append(a)

n.sort()
s = sum(n)
ret = False

for i in range(9):
	if ret:
		break
	for j in range(i+1, 9):
		if (s-n[i]-n[j]) == 100:
			for k in range(9):
				if k==i or k==j:
					continue
				else:
					print(n[k])
			ret = True
			break
