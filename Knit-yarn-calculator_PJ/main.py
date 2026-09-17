import math
print("[대체실 소요량 계산기]",end="\n")
print("[원작 기본 정보]")
size=input("사이즈: ")
og=int(input("원작실 소요량(g): "))
owh=int(input("원작실 1볼/콘 무게(g): "))
olh=int(input("원작실 1볼/콘 길이(m): "))
opls=int(input("원작실 합 수(합): "))
print("[대체실 정보]")
rwh=int(input("대체실 1볼/콘 무게(g): "))
rlh=int(input("대체실 1볼/콘 길이(m): "))
rpls=int(input("대체실 합 수(합): "))
extra=input("50g 추가 구매 여부(y/n): ")
lth=og/owh*(olh/opls)
weh=lth/(rlh/rpls)*rwh
print("[계산 중..]")
print(f"원작실 총 필요 길이: 약 {lth}m\n대체실 예상 필요 무게: 약 {weh}g\n")
balls = math.floor(weh / rwh)
remaining= weh - balls * rwh
if extra=='y':
    e_balls = math.ceil(remaining / 50)
    if e_balls%2==0:
        balls+=1
        e_balls=0
    print(f"대체실 예상 필요 볼/콘 수: {balls}볼/콘")
    print(f"대체실 예상 추가 볼/콘 수: {e_balls}개")
else:
    balls = math.ceil(weh / rwh)
    e_balls = 0
    print(f"대체실 예상 필요 볼/콘 수: {balls}볼/콘")