N, c = map(int, input().split())
result = 1
timeList = input().split()
interval = []

for i in range(N-1):
	if int(timeList[i+1])-int(timeList[i]) >= c+1:
		result = 0
	result += 1

print(result)
