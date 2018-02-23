#-*- coding:utf-8 -*-
'''
    GuraUtil import 
'''

# test.GuraUtil 모듈로 부터 SayHello, SayBte 메소드 import 하기
from test.GuraUtil import SayHello, SayBye
from test.AconUtil import study
from test import AconUtil

# import 된 메소드 사용하기
SayBye()
SayHello()

# import 된 AconUtil 의 변수 참조          메소드 사용
print AconUtil.name, "에서 즐거운" , AconUtil.study()
print "-------------------------"
# import 된 AconUil 의 메소드 사용
AconUtil.study()


print "Step13_import.py 에 들어온 실행순서가 종료 됩니다."