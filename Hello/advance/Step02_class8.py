#-*- coding:utf-8 -*-

class Test:
    
    # 참조값으로 call 할수 있도록
    def __call__(self):
        print "called"

# decorator 를 calss 로 정의하기
class HelloBye:
    # 생성자
    def __init__(self,func):
        self.func=func # 필드에 저장
    # call 되었을때 할 동작
    def __call__(self,*args,**kwargs):
        print "heello"
        self.sing()
        self.dance()
        result=self.func(*args,**kwargs) # decorator된 함수 콜
        print "bye~"
        return result
    def sing(self):
        print "노래를 불러요~"
    def dance(self):
        print "춤을 춰요~"
    
@HelloBye
def test1(): # test1() => func
    print

@HelloBye
def test2():
    print "test2() 호출됨"


if __name__ == '__main__':
    pass
    t1=Test()
    t1() # __call__ 사용 call 가능
    print "------------------"
    test1()
    print "------------------"
    test2()