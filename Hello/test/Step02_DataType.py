#-*- coding:utf-8 -*-
"""
    변수 선언
    
    var num1=10; true false {} javascript
    
    int num1=10; true false  HashMap(key,value) java
    
    num1=10  True False  {key,value} dict type python
"""
# python 참조 data type id값

# int type (정수)
num1=10

# float type (실수)
num2=10.1

# bool type (논리)
isRun=True
isWait=False
isGreater=10>5

# str type (문자열)
myName='kimgura'
yourName="kimgurang"

# unicode type (한글을 다룰때는 unicode type 을 써야한다)
ourName=u'에이콘'
ourName2=u"에이콘 아카데미"

# list type (배열)
# DB에서 수정삭제 하면
nums=[10,20,30,40,50] # int type 을 저장하고 있는 list
names=["kim","lee","park"] # str type 을 저장하고 있는 리스트
friends=[u'김구라',u'해골',u'운숭이'] #unicode type 을 저장

# tuple type (배열) (list type 의 read only(읽기 전에) 버전)
# DB에서 수정삭제 가능성이 없을때 쓰임 속도가 빠름
num2=(10,20,30,40,50)
names2=('kim','Lee','park')
frineds2=(u'김구라',u'해골',u'바람')

# dict type {key,vlaue}  "" 생략 불가
mem1={"num":1, "name":u"김구라", "isMan":True}
mem2={"num":2, "name":u"해골", "isMan":False}

# function type 함수도 객체
"""
    javascript function a(){}
        Python def a():       : => {} 
                   pass
"""
def myFunction():
    pass # pass 꼭 

def b():
    print 'one' # 줄을꼭 맞춰야된다.
    print 'two'
    print 'three'

# b 함수 호출 하는 방법
b()

# b 함수의 참조값을 c에 대입
c=b
    
# None type == null 값  
emptyVar=None # java 의 null 이라고 이해하면 된다.
    
print "Step02_DataType.py 가 종료 됩니다." 