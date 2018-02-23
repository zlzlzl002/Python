#-*- coding:utf-8 -*-
import threading
from pip._vendor import requests


if __name__ == '__main__':
    
    def getHtml(url):
        # get 방식 요청해서 응답 객체를 리턴 받는다
        responseObj=requests.get(url)
        # 응답 문자열 출력해보기 
        print responseObj.text
    
    print " 메인 스레드가 시작됨 "
    
    # 요청 url
    url="http://daum.net"
    
    # get 방식(요청url)
    # responseObj=requests.get("http://daum.net")
    
    # 응답 문자열 출력하기
    #print responseObj.text
    
    
    t=threading.Thread(target=getHtml,args=(url,))
    t.start()
    
    print " 메인 스레드가 종료 됩니다 ."