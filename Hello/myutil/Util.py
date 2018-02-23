#-*- coding:utf-8 -*-

class Pen:
    
    def write(self):
        print "펜으로 필기를 해요"

print "myutil/Util 모듈에 실행순서가 들어왔습니다."
print "Util __name__:" , __name__

if __name__=='__main__':
    print "Util.py 모듈이 main 으로 실행 되었습니다."
    