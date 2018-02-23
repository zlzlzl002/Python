#-*- coding:utf-8 -*-
'''
    로또번호 6개를 무작위로 얻어내서 출력해 보세요~
'''
import random

"""
    Python 모두 객체       기본 Data type 없음
    dict1={}  <=> dict2=dict{}            {}<=이것만 쓰면 빈 dict 로 간주함 
    str=() 빔=""
    int=() 빔=0
    float=() 빔=0.0
    
    !! set2=set{} <= 빈생성자를 콜해야한다 
    tuple1=tuple() <= 빈 tuple 만들 일이없음 수정추가삭제 할수없기때문에
"""

# 로또번호 list [] 담기
nums=set()

"""
while True: 
    # 1~45 사이의 랜던함 정수 
    ranNum =int(random.random()*45)+1 
    nums.add(ranNum)
    if len(nums)==6: # 6개 모두 추출 되었으면
        break # 반복문 탈출
"""

while len(nums)<6:  # <= while 문 특정 조건문  !=6
    ranNum =int(random.random()*45)+1 
    nums.add(ranNum)
    
# set 에 들어 있느 데이터를 list 에 넣기
lottoNums=list(nums) # list 객 체 생성하면서 인자로 set 전달

# 정렬
lottoNums.sort()

for tmp in lottoNums:
    print tmp,    # , 를 붙이면 한줄에 나타남


