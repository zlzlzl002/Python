#-*- coding:utf-8 -*-

class Phone(object): # object 명시해주는게 좋다
    def call(self):
        print "전화를 걸어요"

class HandPhone(Phone): # 상속받는법 (Phone)
    def mobileCall(self):
        print "이동중에 전화를 걸어요"
    def takePicture(self):
        print "100만 화소의 사진을 찍어요"
"""
    Python 다중 상속도 가능하다 ,, 를 붙이면된다 ex) (HandPhone,phone)
    java 는 단일 상속이다
"""
class SmartPhone(HandPhone): 
    def doInternet(self):
        print "인터넷을 해요"
    # 사진찍는 메소드 재정의
    def takePicture(self): 
        # 부모의 메소드 호출 여부
        HandPhone.takePicture(self) # super.takePicture() =java
        print "1000만 화소의 사진을 찍어요"


if __name__ == '__main__':
    pass
    t1=Phone()
    t1.call()
    print "------------------"
    t2=HandPhone()
    t2.call()
    t2.mobileCall()
    t2.takePicture()
    print "------------------"
    t3=SmartPhone()
    t3.call()
    t3.mobileCall()
    t3.doInternet()
    t3.takePicture()