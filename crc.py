from itertools import product
datawords = []

for i in product(['0', '1'], repeat=4):
    d = ''
    for k in i:
        d += k
    datawords.append(d)

for dataword in datawords:
    print(dataword + ":", end=" ")
    input_queue = [0, 0, 0]
    for x in dataword[::-1]:
        input_queue.append(int(x))

    # case 28p -> input_queue = [0, 0, 0, 1, 0, 1, 1]
    r = [0, 0, 0]
    x = [0, 0, 0, 0]  # index number가 차수
    reg_length = 3
    output = 0

    while input_queue:
        s = input_queue.pop()
        x = [output] * 4
        r[2] = r[1]
        r[1] = r[0] ^ x[1]
        r[0] = s ^ x[0]
        output = r[2]

    result = ""

    for x in r:
        result += str(x)

    print(dataword + result[::-1])
