#-*- coding:utf-8 -*-

'''
    함수의 리턴값
'''

# None 이 리턴 되는 함수
def test1(): # 아무것도 없으면 리턴 None
    print "test1()"
    
r1=test1() # None 리턴  
    
# None 이 리턴 되는 함수   
def test2():
    print "test2()"
    return None

r2=test2() # None 리턴

# Int type 을 리턴 해주는 함수
def test3():
    print "test3()"
    return 10

# Dict type 을 리턴 해주는 함수
def test4():
    print "test4()"
    return {"num=999"}

r4=test4() # Dict type

# List type 을 리턴 해주는 함수
def test5():
    print "test5()"
    names=['kim','park','lee']
    return names

r5=test5() # list type

# function type 을 리턴 해주는 함수   
def test6():
    print "test6()"
    def a():
        print "a()"
    return a

r6=test6() # r6 는 function type 이므로

r6() # 호출할수 있다.

print "Step06_function6 가 종료 됩니다."

