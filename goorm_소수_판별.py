import math

n = int(input())

if math.sqrt(n).is_integer():
	print(False)
else:
	for i in range(2, round(math.sqrt(n))):
		r = n % i
		if r == 0:
			print(False)
			break
	if r != 0:
		print(True)
			
