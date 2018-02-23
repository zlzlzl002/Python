#-*- coding:utf-8 -*-

"""
    정규 표현식으로 매칭되는 모든 문자열 찾기
"""
import re

msg ='monday tuesday wednesday thursday friday saturday sunday'

if __name__ == '__main__':
    
    Reg="[a-z]*day" # *는 0번이상
   
    # pattern 에 매칭되는 모든 문자열을 찾아서 list 로 리턴해준다
    m=re.findall(Reg, msg)
 
    print m     # list type
    
    print "pattern 에 매칭되는 문자열의 갯수:", len(m)
    print "- 매칭되는 문자열 목록-"
    for tmp in m :
        print tmp,
    
    
    
    