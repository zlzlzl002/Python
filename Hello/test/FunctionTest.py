#-*- coding:utf-8 -*-

# 함수 생성 하기
def test1():
    pass 

# 함수 호출하기
test1()

# 줄을 맞춰줘야 한다  
def test2():         # : 들여쓰기는   == {}
    print "gura"
    print "gura2"
    print "gura3"
    
# arg 인자를 전달하는 함수 생성
def test3(arg):
    print "arg:", arg

# test3() 한개 인자라도 전달안하면 안된다. 오류남
# test3("gogo","gogogo") 1개의 인자만 전달가능 사용하려면 *args 
test3("gogo")

# 인자를 2개 전달하는 함수 생성
def test4(a,b):
    print "a:", a, "b:", b

test4(1,2)

# *args 전달하는 함수 생성
def test5(*args):
    # tuple type 이다
    print "args:", args

test5() # *args 인자를 절단 안해도되고
test5(1) # *args 인자를 1개만 전달해도 된다 그이상도 가능
test5('kim','lee')

# **kwargs keyword arguments
def test6(**kwargs):
    # Dict type 이다
    print "kwargs:", kwargs
    
test6()
test6(num=2,name="gura")
test6(num=3,name="gura2",isMan=True)

# *args **kwargs 같이 사용하기
def test7(*args, **kwargs):
    print "args:",args , "kwargs:", kwargs

test7()
test7(1)
test7(name="mouse")
test7(2,name="key")

# 
def test8(num,name,addr):
    print "num:",num, "name:",name, "addr:",addr
test8(num=1,name="kim",addr="sa") #key
test8(2,"gugu","gogogo")

print "------------------------------"

def test9(num=0,name="",addr=""):
    print "num:",num, "name:",name, "addr:",addr
test9(num=1,name="gogo",addr="gogogo")