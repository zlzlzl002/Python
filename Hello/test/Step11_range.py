#-*- coding:utf-8 -*-
'''
    range 함수 사용하기
'''

# range(10) => 0~9 까지 list return 해준다 
result1=range(10) # range함수

print "result1:", result1

# range(15) => 0~14 까지 list return 해준다
result2=range(15)

print "result2:", result2

#range(start(이상),end(미만),step(증가값)) => for문
result3=range(0,10,1)
print 'result3:', result3

result4=range(0,10,2)
print 'result4:', result4
