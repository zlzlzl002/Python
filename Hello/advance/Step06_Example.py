#-*- coding:utf-8 -*-
import re


if __name__ == '__main__':
    
    inputMsg=raw_input(u'영문자 소문자만 입력:')
    
    result=inputMsg.decode('utf-8')
    
    pattern='^[a-z]+$'
    
    m=re.search(pattern,result)
    if bool(m): # None=False bool type  == # if m: 결과는 같다.
        print" 잘 입력 했습니다."
    else:
        print " 영문자 소문자만 입력하세요"