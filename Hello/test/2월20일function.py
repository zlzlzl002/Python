#-*- coding:utf-8 -*-
"""
    Python 
    : 들여쓰기는 == {} 같다  
"""
# 함수
def a():
    pass # 아무것도 정의 안할때 pass

a() #  a() 함수 콜하는법

def b(arg1):
    print "arg:", arg1
# b() 인자를 전달안하면 오류남
b(1)


def c(*args):
    # tuple type
    print "*arg", args

c(10)
c(10,20)
c(10,20,30)

# keword 
def d(**kwargs):
    # Dict type
    print "kwargs:", kwargs

d(name="gura")
d(num=1,name="gura")
    
# tuple Dict type 같이 사용하고싶을때
def e(*args,**kwargs):
    print "args:",args, "kwargs:",kwargs

e()
e(1)
e(num=2) 
e(1,name="gura")

# 대입
def f(num,name,addr):
    print "num:",num,"name:",name,"addr:",addr

f(num=1,name="gura",addr="sang")
    
    
    
    
    