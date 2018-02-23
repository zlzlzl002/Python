#-*- coding:utf-8 -*-
"""
    java Class Car{
        String name:   1. type name 미리선언
        
        public Car(){
            this.name="gura";
        }
    }    
    
    java 와 python 다른점은 java 는 미리 필드 선언을하고
    python 미리 선언을 하지않는다. 
    
"""

class Car:
    #self 는 heap 영역에 생긴 참조값을 전달받는다.
    def __init__(self,name2): 
        # 객체를 생성할때 생성자에 전달되는 인자를 필드에 저장한다.
        self.name=name2 # self. 필드 추가 (동적)
        
        # 메소드
        def showInfo(self):
            info="이 차의 제조사는 {} 입니다.".format(self.name)
            print info
            
# 생성자 호출 
c1=Car("gura")  # ("gura")는 생성자인자 name2 전달된다
c2=Car("kia")

print "c1.name :" , c1.name
print "c2.name :" , c2.name

c1.showInfo()
c2.showInfo()