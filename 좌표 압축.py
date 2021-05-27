n = int(input())
data = list(map(int, input().split()))
data_set = sorted(list(set(data)))
length = len(data_set)
calc = {}

for i in range(length):
    calc[data_set[i]] = i

for j in range(n):
    print(calc[data[j]], end=" ")
