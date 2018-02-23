#-*- coding:utf-8 -*-
'''
    decorator 는 함수의 장식자 이다.
'''

# decorator 로 사용할 함수 정의하기
def helloBye(func):
    # 인자로 전달된 func 에는 장식된 함수의 참조값이 전달된다.
    def wrapper():
        # 장식된 함수의 코드를 수행하기 이전에 할 작업
        print "hello"
        func() # 장식이된 함수를 호출 하는 함수
        # 장식된 함수의 코드를 수행한 이후에 할 작업
        print "Bye"
    return wrapper()

# f1 함수를 helloBye decorator 함수로 장식하기
@helloBye
def f1():
    print "f1() 수행됨"

print "-----------------"
    
@helloBye
def f2():
    print "f2() 수행됨"
    
print"-----------------"
    
@helloBye
def f3():
    print "f3() 수행됨"

# f1,f2,f3 함수 콜
#f1()
#f2()
#f3()