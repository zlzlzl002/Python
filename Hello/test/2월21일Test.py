#-*- coding:utf-8 -*-
import random

num=set()

while len(num) <6:
    ranNum=int(random.random()*45)+1
    num.add(ranNum)

lotto=list(num)

lotto.sort()

for tmp in lotto:
    print tmp,