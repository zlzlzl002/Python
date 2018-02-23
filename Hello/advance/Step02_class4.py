#-*- coding:utf-8 -*-

# import 하는 시점에 실행순서가 1번들어온다 Util 8/9번째줄 실행
from myutil.Util import Pen


# __xxx__ 정해진값
if __name__ == '__main__':
    
    print '모듈이 main 으로 실행되었습니다.'
    # 외부 모듈에 있는 클래스를 import 해서 객체 생성
    pen1=Pen()
    # 메소드 호출
    pen1.write()