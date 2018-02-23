#-*- coding:utf-8 -*-

'''
    custom 예외 발생 시키기
    
    - 프로그래머가 의도하는 시점에 직접 예외를 발생 시킬수 있다.
    
    raise 예외 처리
    
'''

if __name__ == '__main__':
    
    print " 메인 스레드가 시작 되었습니다. "
    try:
        msg=input("정수 입력:")
        
        if not isinstance(msg,int) :
            # 프로그래머가 원하는 시점에 직접 예외 발생 시키기
            raise ValueError(" 정수를 입력하라니까 말을 안듣네~~")
        print "입력한 정수:",msg
    except ValueError, ve:
        print ve
    print " 메인 스레드가 종료 됩니다."