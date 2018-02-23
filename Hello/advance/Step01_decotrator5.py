#-*- coding:utf-8 -*-

def auth(func):
    # 장식된 함수에 전달되는 모든 인자를 받을 준비
    def wrapper(*args,**kwargs):
        
        value=func(*args,**kwargs)
        # 장식된 함수가 리턴해주는 값을 리턴할 준비
        if kwargs["userId"]=="gura":
            value="success"
        return value
    return wrapper
        
@auth
def test1(userId):
    print "test1() 호출됨"
    return "fail" # fail값은 => value=fail

result=test1(userId="gura") # kwargs 인자로
print "result:", result

print "Step01_decorator5.py 가 종료 됩니다."