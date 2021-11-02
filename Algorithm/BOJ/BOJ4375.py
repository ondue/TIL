#TODO: 1

while True:
	try:
		n = int(input())
	except:
		break
	ret = 1
	num = 0

	while True:
		num = num*10 + 1
		num %= n
		if num == 0:
			print(ret)
			break
		ret+=1
