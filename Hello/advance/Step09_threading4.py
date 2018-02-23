#-*- coding:utf-8 -*-
import threading
from pip._vendor import requests

# Thread 클래스를 상속 받아서 클래스 정의하기
class myThread(threading.Thread):
    # 생성자
    def __init__(self,url):
        # 부모의 생성자에 필요한 값 전달하기 (부모생성자 호출)
        threading.Thread.__init__(self)
        # 인자로 전달된 url 을 필드에 저장
        self.url=url
        
    # 스레드의 본체가 되는 run() 메소드 재정의하기
    def run(self): # def run 부모의 run 메소드 오버라이
        reponseObj=requests.get(self.url)
        print reponseObj.text

if __name__ == '__main__':
    
    print " 메인 스레드가 시작됨 "
    
    # 요청 url
    url="http://daum.net"
    
    t1=myThread(url)
    # 데몬 쓰레드는 메인 스레드가 종료되면 같이 종료 된다.
    # t1.daemon=True  # 기본값 False
    t1.start()
   

    
    print " 메인 스레드가 종료 됩니다 ."
    
