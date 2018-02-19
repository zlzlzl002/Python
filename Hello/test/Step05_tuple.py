#-*- coding:utf-8 -*-

"""
    - tuple
    
    1. list type 의 read only 버전(읽기전용)
    2. 수정, 삭제 불가
    3. list type 보다 처리 속도가 빠르다.
"""

tuple1=(10,20,30,40,50)

for tmp in tuple1:
    print "tmp:", tmp 

# 수정불가
# tuple1[0]=999

# 삭제불가
# del tuple1[0]

# 방 1개 짜리 tuple type 을 만들때는 주의!
result=('kim',) # tuple 방1개짜리는 , 를 붙여 줘야된다.
# result=('kim') <= str이다 tuple 아님

# tuple 을 만들때 ( ) 는 생략 가능  
result2=u"김구라", u"해골", u"원숭이" 

# tuple 을 출력 
print u"하나", u"두울", u"세엣"

# 두개의 변수에 값 한번에 할당 하기
a, b = 10, 20

# 두변수에 있는 내용을 상호 교환 하려면?
first="girl"
second="boy"

"""
tmp=first
first=second
second=tmp
"""

# 두변수 상호 교환 하는법
first, second =second, first # first=boy, second=girl



print "Step05_tuple.py 가 종료 됩니다."