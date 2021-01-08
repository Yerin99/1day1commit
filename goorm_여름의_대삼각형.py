# goorm - 여름의 대삼각형
# python3으로 구현
#
# 평면 좌표에서 세점을 알 때 넓이 구하는 공식은
# 세점을 (a,b) (c,d) (e,f) 라 하면 
# 1/2 *ㅣad+cf+eb-bc-ed-afㅣ 

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
result = 0.5*abs(a*d+c*f+e*b-b*c-e*d-a*f)
print("{0:.2f}".format(result))
