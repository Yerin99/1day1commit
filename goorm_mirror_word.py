def isMirror(word):
    org_word = word
    m_word = ""
    string1 = "bilmnopsuvwx"
    string2 = "dilmnoqzuvwx"
    for element in org_word:
        if element in string1:
            i = string1.index(element)
            m_word += string2[i]
        elif element in string2:
            i = string2.index(element)
            m_word += string1[i]
        else:
            return False
    if org_word == m_word[::-1]:
        return True
    else:
        return False

n = int(input())    # 받을 단어의 갯수

for i in range(n):
    word = input()
    if isMirror(word):
        print("Mirror")
    else:
        print("Normal")
