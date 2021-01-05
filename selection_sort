n = int(input())
line = input()
numlist = list(map(int, line.split()))

for i in range(n):
	minnum = numlist[i]
	index = i
	for j in range(i, n):
		if numlist[j] < minnum:
			minnum = numlist[j]
			index = j
	numlist[i], numlist[index] = numlist[index], numlist[i]
	
for i in range(n):
	print(numlist[i], end=" ")
