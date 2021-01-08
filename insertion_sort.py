n = int(input())
line = input()
numlist = list(map(int, line.split()))

for i in range(n-1):
	for j in range(i+1, n):
		if numlist[i] > numlist[j]:
			numlist[i], numlist[j] = numlist[j], numlist[i]
		
for i in range(n):
	print(numlist[i], end=" ")
	
