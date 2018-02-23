#-*- coding:utf-8 -*-

'''
    문자열 format
   format 구조  def format(*args, **kwargs): 
'''

result1=u"내이름은 {} 입니다.".format(u"김구라")
print "result1:", result1

# tuple type 으로 받아들인다.
result2=u"cat:{0}, dog:{1}".format(u"고양이",u"강아지")
print "result2:", result2

# {} 안에 index 를 명시 하지 않아도 순서대로 들어간다.
result3=u"cat:{}, dog:{}".format(u"고양이",u"강아지")
print "result3:", result3

# .format(0번째(강아지) 1번째(고양이))
result4=u"cat:{1}, dog:{0}".format(u'강아지',u'고양이')
print "result4:", result4







