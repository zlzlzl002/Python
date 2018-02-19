#-*- coding:utf-8 -*-

'''
    함수에 인자 전달하기
'''

# arg1 인자를 갖고있는 함수 test1 생성
def test1(arg1):
    print "arg1:",arg1

#test1()  test1 함수 호출 오류

test1('kim') # test1('kim') 함수 호출

# a,b 인자를 갖고있는 함수 test2 생성
def test2(a,b):
    print "a:",a,  "b:",b

test2('dog','cat') 

print "Step06_function2.py 가 종료 됩니다."
