def main():
	a,b = input().split(" ")
	maxnum, val = 0, 0
	dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }

	if a == b:
		a = int(a)
		if a < 10:
			return int(a)+1
		else:
			return 10
	
	for x in b:
		if x.isalpha():
			x = dic[x]
		x = int(x)
		if maxnum <= x:
			maxnum = x
	
	maxnum += 1
		
	a = int(a)
	b = b[::-1]

	for i in range(maxnum, 17):
		for index, x in enumerate(b):
			if x.isalpha():
				x = dic[x]
			val += int(x)*(i**index)
		if val == a:
			return i
		val = 0
		
print(main())
