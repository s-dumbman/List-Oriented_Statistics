import random
import time
# VAR set zone
a = 0
b = 101
c = 5
v2 = 9090
if c<0:
    print("Error type 1 // Range가 정의되지 않습니다.")
    print(c,"<",0,"        ^^^^^^")
    time.sleep(v2)
if a ==b:
    print("Error type 2 // Max와 Min의 값이 정의되지 않습니다.")
    print(a,"==",b,"       ^^^^^^")
    time.sleep(v2)
if a>b:
    print("Error type 3 // Max와 Min의 값이 정의되지 않습니다.")
    print(a,"<",b,"        ^^^^^^")
    time.sleep(v2)
def percent():
    print("범위 설정 //","Min:",a,"/ Max:",b,"/ Range:",c)
    for i in range(1):
        ran = [random.randrange(a, b) for i in range(c)]
        print("선택 범위 섹션 //", ran)
        time.sleep(1)
        print("확률 분석 //", 100 * (1 / b), "% (", a, "~", b - 1, "까지의 근사 확률 // 단독명령을 제외한 계산값 )")
        time.sleep(2)
        if i in range(1):
            print("선택 범위 섹션에서 최종적으로 선택된 값 // <", random.choice(ran), ">")
if __name__=='__main__':
    percent()


