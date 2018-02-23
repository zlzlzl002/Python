#-*- coding:utf-8 -*-

nameSet={'kim','lee','park'}

# set 에 'kim' 이 존재하는지 여부
result1= 'kim'in nameSet # bool type 으로 받는다
# set 에 'kim' 이 존재하지 않은지 여부
result2= 'kim' not in nameSet

print "result1:",result1
print "result2;",result2

# list 에서 중복을 제거할때 사용할수 있다.
nums=[10,10,20,20,30,30,40,50]

# 빌트인 set 클래스를 이용해서 중복 제거된 set 얻어내기
set1=set(nums)  # !! set() => set() class 객체 생성

'''
    - set class 정의 (Python)     (JAVA)               
    class set :                 class Set{
        def _init_(): <= 생성자        public Set(){
      호출 set()                    }}       호출 new set()
'''

print set1

# 빌트인 list 클래스를 이용해서 set 을 list 로 얻어내기
nums2=list(set1)

print "num2:",nums2

# 정렬
# nums2.sort() 
nums2.sort(reverse=True) # 역순 정렬 
print "정렬후 nums2"
print nums2


print "Step07_set2.py 가 종료 됩니다."
