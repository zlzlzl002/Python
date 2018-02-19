#-*- coding:utf-8 -*-

"""
    - List type
    
    1. 순서가 있다 (인덱스로 데이터를 관리한다)
    2. 여러개의 데이터를 저장할수 있다.
    3. 값 변경 가능
"""
from __builtin__ import len

#       0번         1번      2번
family=[u"엄마",u"아빠",u"나"]

# 데이터 추가
family.append(u"남동생")
family.append(u"여동생")

# 데이터 삭제
del family[3] # 인덱스를 이용한 삭제

# 데이터 삭제
family.remove(u"여동생") # 값에 의한 삭제

# 데이터 수정
family[0]=u"맘" # 인덱스를 이용한 수정

# 가장 마지막 방의 내용을 가져오기
result=family.pop()

nums=[50,30,40,20,10]

# 오름차순 정렬
nums.sort()
# 내림차순 정렬 reverse 기본값은 false
nums.sort(reverse=True) # keyword argument=reverse

for tmp in nums:
    print "tmp:",tmp
    
# 배열의 방의 갯수
print "len(nums) : ", len(nums)

print "Step04_List.py 가 종료 됩니다."