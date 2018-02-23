#-*- coding:utf-8 -*-
'''
        정규 표현식(Reg) 사용 하기 
'''
import re




if __name__ == '__main__':
    
    # 검증할 문자열
    msg="Hello, world"
    
    # import 된 정규 표현식 객체(re) 의 메소드를 이용한다.
    # re.search(정규표현식, 검증할 문자열)
    
    # 검증할 문자열에서 정규 표현식에 매칭되는 문자열이 있으면
    # Match 객체가 리턴된다.
    result=re.search("Hello", msg) # Match Object
    
    if result:
        print "Hello 를 찾았습니다."
    else :
        print "Hello 를 찾지 못했습니다."
    
    # 없으면 None == null
    result2=re.search("hello", msg) # None == null
    
    """
        bolltype 말고 참조값으로 할수있다.
        
        if true: 
        if 참조값: 있으면 True 없으면 False
        if false:
        if None:
    """
    
    if result2: # bool type 은 아니다.  
        print "hello 를 찾았습니다."
    else :
        print "hello 를 찾지 못했습니다."
    
    print "result:", result
    print "result2:", result2
    
    
    
    
    
    
    
    
    
    
    print "Step06_RegExp.py 가 종료 됩니다."