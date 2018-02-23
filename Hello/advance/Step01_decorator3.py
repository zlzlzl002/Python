#-*- coding:utf-8 -*-

def myDeco(func):
    def wrapper(*arg): 
        if arg=="김구라":
            arg="개구리"
        func(*arg) # => test1(arg==name)
    
    return wrapper

@myDeco
def test1(name, bb):
    print "name:", name, bb
    print "test() 수행됨"
    
test1("김구라") # => def wrapper("김구라")
print "------------------"
test1("해골")
print "------------------"
test1("원숭이")

@myDeco
def test2(a,b): # myDeco 인자를 *arg로 
    print a,b   # 지금은 오류나옴
 
test2("김구라","바보" )