#-*- coding:utf-8 -*-

# Dict(dictionary) 순서가없는 데이터 type == javascript object type 유사 

mem1= {"num":1, "name":"kimgura", "addr":"zoo"}

# 특정방 참조하기
a=mem1["num"]
print a

# num 수정 해보기
mem1["num"]=999

# num 삭제 해보기
del mem1["num"]

result =mem1.keys()

# key 값 
for tmp in mem1.keys():
    print tmp, ":" ,mem1[tmp] 

# tuple  정보 수정 삭제 할수 없다 List type 보다 빠르다
num=(1,2,3,4,5)


# del num[1] tuple type 이런거 안됨

for tmp in num:
    print "tmp:", tmp

# 방 1개 짜리 tuple 만들때 ,
result=("kim",)

# 여러개 한번에 할당하기
a, b ,c = 10,20,30
print a,b,c

# 서로 바꾸기
myName="ansdj"
yourName="ansdj2"

myName , yourName= yourName, myName
print "myName:", myName, "yourName:" , yourName

# list type 방번호 생각하시옹
name=["kim","lee","park"]

# 추가하기
name.append("Moon")

# 삭제하기
del name[0]

# 수정하기
name[0]="Han"

# 오름 차순 정렬 하는법
nums=[10,20,40,50,30,60]
nums.sort()
for tmp in nums :
    print tmp

# nums 방의 갯수 구하기
print len(nums)



