#TODO: 회전하는 큐

N, M = map(int, input().split())
ret = list(map(int, input().split()))
lst = list(range(1, N+1))
cnt = 0

def left_move(lst):
	lst.append(lst[0])
	lst.remove(lst[0])
	global cnt
	cnt += 1
	return lst

def right_move(lst):
	lst.insert(0, lst[-1])
	lst.pop()
	global cnt
	cnt += 1
	return lst

while ret:
	if lst[0] == ret[0]:
		lst.pop(0)
		ret.pop(0)
	else:
		if lst.index(ret[0]) <= len(lst) // 2:
				while lst[0] != ret[0]:
					left_move(lst)
		else:
			while lst[0] != ret[0]:
				que = right_move(lst)

print(cnt)
