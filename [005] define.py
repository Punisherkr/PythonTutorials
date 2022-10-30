from cgitb import text
from typing import Text


print("김보성은 조만간 부자가 될 것이다.")
print("김보성은 조만간 부자가 될 것이다.")
print("김보성은 조만간 부자가 될 것이다.")
print("김보성은 조만간 부자가 될 것이다.")
#cntl+alt+위아래방향키로 같은 문단위치로 위아래 동시 편집 가능



#def = define
def print_김보성():
    text = "김보성은 2022년 로또 1등 80억 이상 당첨된다"
    print(text)
    print(text)
    print(text)

print_김보성()
#def로 먼저 정의 한 후에 Print_@@@ function 사용 가능하므로
#def 문법으로 정의 하고 그보다 아래줄에 print_@@@ function 기능 사용하다
#def 기능은 def로 정한 코드를 압축하여 다음에 반복할때 다시 코드를 쓸 필요 없게 
#def로 정한 코드를 쓴다.

def print_보성(text5):
    print(text5)
    print(text5)
    print(text5)

print_보성("보성이는 대기만성형 성공 곧 한다. text5 ")


def print_1(text1):
    print(text1)
    print(text1)

print_1("definition 1")



def print_2(text2):
    #print(text1) 현재 문단은 text2관련 definition을 정하는 소문단이라
    #위에서 지정한 text1 variable은 작동하지 않는다.
    print(text2)
    print(text2)

    
print_2("definition 2")
