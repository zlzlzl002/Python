#-*- coding:utf-8 -*-

'''
    함수를 호출할때 전달하는 keyword 인자를 dict 로 받을수 있다.
'''

# kwargs : keyword arguments 키워드로 전달하는 인자들의 약자
def test1(**kwargs): 
    # kwargs dict type 이다
    print kwargs

test1()
test1(num=1)
test1(num=2,name="kimgura")
test1(num=3,name="gurazang",addr="zoo")

# 오류 발생 (keyword 인자가 아니므로)
# test1("one","two")

print "---------------------------------"

# 어떤 형태의 호출도 다 받아 줄수 있는 형태의 함수
def test2(*args, **kwargs):
    print args, kwargs

test2()
test2(10)
test2(num=1)
test2(20, num=2)