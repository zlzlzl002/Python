#-*- coding:utf-8 -*-
"""
    class 정의하기
    self == java(this)
    self => 예약어는 아니다.
"""

# !! [ Car 클래스 정의하기 ]
class Car:       # public class Car{} <=java
    # !! [ 생성자 ]
    def __init__(self):
        print "Car 클래스의 생성자 호출됨"
    # 메소드 정의하기
    def drive(self):
        print "부릉부릉~"
    
# 클래스를 이용해서 객체를 생성해서 참조값을 c1 변수에담기        
c1=Car() # new Car() <= java
# c1 변수에 담겨 있는 참조값을 이용해서 객체의 메소드 호출
c1.drive()
 
print "id(c1) :", id(c1)






print "Step02_class.py 가 종료 됩니다."