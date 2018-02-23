#-*- coding:utf-8 -*-
'''
    모듈을 만들때 main 으로 만듬
'''

class Coffee:
    def drink(self):
        print " 커피를 마셔요 "

class StarBucks:
    # 생성자의 인자로 전달되는 지점명을 branch 라는 필드에 저장하기
    def __init__(self,branch):
        self.branch=branch
    
    # Coffee 객체를 생성해서 리턴해주기
    def getCoffee(self):
        # coffee=Coffee()
        # return coffee
        return Coffee()
    
    
    # count 가 정수 일때 해당 숫자만큼 Coffee 객체를 생성해서
    # 참조값을 list type 에 담아서 list 를 리턴해주기
    def getCoffees(self,count):
        # 빈 list 를 만들어서
        coffeeList=[]
        # count 숫자만큼 반복문 돌아서
        for i in range(count):
            # Coffee 객체를 생성해서
            tmp=Coffee()
            # list 에 누적 시키고
            coffeeList.append(tmp)
            # coffee 객체의 참조값이 들어 있는 list 를 리턴해준다.
            return coffeeList
        
    # 지점명을 콘솔창에 출력하기
    def showInfo(self):
        print "지점명: {}",format(self.branch)

if __name__ == '__main__':
    pass

    # 1. StarBucks 객체를 생성해서 참조값을 변수에 담기 (지점:종각)
    c1=StarBucks(branch="종각")
    # 2. getCoffee() 메소드를 호출해서 리턴되는 Coffee 객체의
    # .drink() 메소드를 호출해 보세요
    c1.getCoffee().drink()
    # 3. getCoffees() 메소드를 호출하면서 5를 전달하고 리턴되는
    # list 객체에 있는 Coffee 객체의 .drink() 메소드를 모두 호출
    coffeeList=c1.getCoffees(5)
    for tmp in coffeeList:
        tmp.drink()
    # 4. showInfo() 메소드 호출
    c1.showInfo()
    
    
    
    
    
    
    
    
    