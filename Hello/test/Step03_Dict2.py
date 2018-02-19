#-*- coding:utf-8 -*-

# 회원 한명의 정보를 dict 에 담기
mem1={"num":1,"name":u"코알라","addr":u"호주"}

# dict 의 모든 key 값을 list 로 얻어내기
result=mem1.keys()

# dict 에 담긴 모든 내용을 콘솔에 출력해보기
for tmp in mem1.keys(): # : 들여쓰기는 블럭 의미  => javascript {}
    print tmp, " : ",mem1[tmp] # 임시 변수라고도 할수있다.

# dict 의 모든 value 값을 list 로 얻어내기
result2 =mem1.values()

# dict 에 담긴 모든 애용을 콘솔에 출력해보기
for b in mem1.values():
    print b    
    