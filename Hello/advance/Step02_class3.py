#-*- coding:utf-8 -*-

class MemberDto:
    
    # 생성자
    def __init__(self, num, name, addr):
        self.num=num
        self.name=name
        self.addr=addr
        
    def setNum(self,num):
        self.num=num
    
    def getNum(self):
        return self.num
    
    def setName(self,name):
        self.name=name
    
    def getName(self,name):
        return self.name
    
    def setAddr(self,addr):
        self.addr=addr
    
    def getAddr(self,addr):
        return self.addr
    
mem1=MemberDto(1,u'김구라',u'노량진')
mem2=MemberDto(2,u'해골',u'행신동')
mem3=MemberDto(3,u'원숭이',u'종로')






print "Step01_class.py 가 종료 됩니다."   
    