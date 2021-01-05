n = int(input())
line = input()
numlist = list(map(int, line.split()))


for i in range(n-1):
	for j in range(n-1-i):
		if numlist[j] > numlist[j+1]:
				numlist[j], numlist[j+1] = numlist[j+1], numlist[j]
		
for i in range(n):
	print(numlist[i], end=" ")
