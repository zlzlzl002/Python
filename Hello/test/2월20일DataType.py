#-*- coding:utf-8 -*-

# Dict type
mem1={"num":1,"name":"gura","addr":"hong"}

# 삭제하기 
del mem1["num"]

# 수정하기
mem1["num"]=2

# tuple type      수정/삭제 불가  list type 속도 빠름
a=(1,2,3,4)

# 여러값 넣기
a,b=10,20

# 1개 생성할때는 , 를 붙여 줘야한다
a=(1,) 

# 두변수 상호 교환
isMan="guzn"
isGirl="sang"

isMan, isGirl=isGirl, isMan
print "isMan:",isMan, "isGirl:",isGirl

# list type
int1=[1,2,3,4,5]

# 한개방 참조하기
a=int1[0]

# 삭제하기
del int1[1]

# 추가하기
int1.append(6)

# 정렬
# int1.sort() 오름차순
int1.sort(reverse=True)

# 배열의 방의 갯수
print "len(int1) 갯수:", len(int1)
