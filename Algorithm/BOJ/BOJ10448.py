#TODO: 유레카 이론

tri = [n * (n+1) // 2 for n in range(1, 46)]
urk = [0] * 1001

for i in tri:
	for j in tri:
		for k in tri:
			if i + j + k <= 1000:
				urk[i+j+k] = 1

for i in range(int(input())):
	print(urk[int(input())])
