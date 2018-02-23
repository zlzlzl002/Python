#-*- coding:utf-8 -*-
"""
    java = static 비슷
"""
# 가상의 공격 유닛을 생성할 클래스
class AttackUnit:
    # 모든 객체가 공유할 클래스 변수 만들고 초기값 부여
    attackPower=10 
    
    # 공격하는 인스턴스(객체의) 메소드
    def attack(self):
        print "{} 의 파워로 공격 합니다."\
            .format(AttackUnit.attackPower)

if __name__ == '__main__':
    pass
    
    # 클래스 변수는 클래스명으로 접근해서 참조할수 있다.
    print AttackUnit.attackPower
    # 클래스 변수의 값 수정하기
    AttackUnit.attackPower=20
    print AttackUnit.attackPower
    
    # 참조값으로 호출하는 메소드 인스턴스(객체)
    unit1=AttackUnit()
    unit1.attack()
    
    
    
    
    
    
    
    