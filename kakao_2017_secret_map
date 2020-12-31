# 2017 카카오 1차 코딩 테스트
# 1번 문제 - 비밀 지도
# 난이도 : 하 

n = int(input())
arr1, arr2 = eval(input()), eval(input())
result1, result2 = [], []

for i in range(n):
    binar2 = bin(eval(bin(arr1[i])) | eval(bin(arr2[i])))
    print(binar2)
    result1.append(binar2)

for i in range(n):
    string = ""
    for index, x in enumerate(result1[i]):
        if x == 'b':
            continue
        elif int(x) == 0 and index != 0:
            string += ' '
        elif int(x) == 1:
            string += '#'
    while len(string) != n:
        string = " " + string
    result2.append(string)

print(result2)
