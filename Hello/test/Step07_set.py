#-*- coding:utf-8 -*-

'''
    - set 
    1. 순서가 없다
    2. 중복을 허용하지 않는다.
    3. 집합(묶음) 이라고 생각하면 된다.
'''

set1={10,20,30,40,50}

# 데이터 추가하기
set1.add(60)
set1.add(70)
# 중복 데이터는 들어가지 않는다.
set1.add(70)
set1.add(60)
set1.add(10)

# 저장된 갯수는 len() 메소드를 이용한다.
print "len(set1):", len(set1)

set2=(60,70,80,90,100)

# set1 합집합(union) set2
result1=set1.union(set2)

# set1 교집함(intersection) set2
result2=set1.intersection(set2)

# set1 차지합(-) set2
# result3=set1-set2

# 동물의 집합
animalSet={'cat','dog','snake','lion','tiger'}

# 집합에서 특정값 삭제
animalSet.discard('snake')
# .discard() 는 삭제할 데이터가 없으면 무시한다.
animalSet.discard('elephant')

# 삭제하는 방법 2
animalSet.remove("cat")
# .remove() 는 삭제할 데이터가 없으면 예외(Except)를 발생 시킨다.
# animalSet.remove("frog")

# 모든 내용삭제
animalSet.clear()

nameSet={"Lee","kim"}

list1=['park','song']
tuple1=('jo','name')

# set 에 list 나 tuple 을 병합 시킬수 있다
nameSet.update(list1)
nameSet.update(tuple1)

print nameSet

# 반복문 돌면서 모든값 하나씩 사용해 보기
for tmp in nameSet:
    print tmp
    
    
    

print "Step07_set.py 가 종료 됩니다."