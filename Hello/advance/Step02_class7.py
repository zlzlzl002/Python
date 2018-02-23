#-*- coding:utf-8 -*-

# 가상의 공격 유닛을 생성할 클래스
class AttackUnit:
    # 모든 객체가 공유할 클래스 변수 만들고 초기값 부여
    attackPower=10 
    
    # 공격하는 인스턴스(객체의) 메소드
    def attack(self): # class 명으로 접근할수 없고 참조값으로 접근할수있다.
        print "{} 의 파워로 공격 합니다."\
            .format(AttackUnit.attackPower)
            
    # class(객체) 메소드 만드는 방법
    @classmethod #(decorator)
    def setPower(cls,power): # cls => class 참조값
        # 첫번째 인자로 클래스의 참조값이 들어온다.
        cls.attackPower=power
        # AttackUnit.attackPower=power
    
    @classmethod
    def showPower(cls):
        print "현재의 공격력 : {} ",format(cls.attackPower)

if __name__ == '__main__':
    
    unit1=AttackUnit()
    unit2=AttackUnit()
    unit3=AttackUnit()
    
    # 클래스 메소드를 클래스명으로 사용해보기
    AttackUnit.showPower()
    AttackUnit.setPower(20)
    AttackUnit.showPower()
    
    print "--- 클래스 메소드를 이용해서 클래스 변수 수정후---"
    unit1.attack()
    unit2.attack()
    unit3.attack()
    
    
    
    