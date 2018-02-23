#-*- coding:utf-8 -*-

"""
      함수에 여러개의 인자를 동적으로 전달하기
    *args => 인자를 전달 안해도되고 여러개해도 가능
"""

def test1(*args): # arguments 약자 : args 인자들
    # args 는 tuple type 이다.
    print args
    
#test1() tuple 
test1()
test1(10) #tuple 10, 
test1(10,20) 
test1(10,20,30)
test1("one","two",True)
    
print "Step06_function3.py 가 종료 됩니다."
