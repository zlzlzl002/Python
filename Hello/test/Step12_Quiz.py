#-*- coding:utf-8 -*-

'''
    input() 함수를 이용해서 숫자를 입력 받아서 
    
    2 를 입력하면 구구단 2단 출력
    3 을 입력하면 구구단 3단 출력
    .
    .
    
      하는 코드를 작성해 보세요
    
      출력 형식 
    
    - 구구단 2단 -
    2x1=2
    2x2=4
    2x3=6
'''

result1=input("입력:")

info=u"-구구단 {} 단 -".format(result1)

print info

for i in range(1,10):
    print result1, "*", i, "=" ,result1*i
    
    
    