import random
import numpy as np
import time
class Gem:
    name=""
    rarity=0
    value=0
    def __init__(self):
        tiervalues={0:random.randint(1,10),0.125:random.randint(10,20),
        0.25:random.randint(20,40),0.5:random.randint(40,80),
        0.75:random.randint(80,160),0.875:random.randint(160,320),
        0.984375:random.randint(320,1000)}
        self.name="".join([random.choice("qwertyuiopasdfghjklzxcvbnm") for x in range(random.randint(2,10))]).capitalize()
        rarity=random.random()
        table=[rarity>=x for x in tiervalues.keys()]
        self.rarity=(len(tiervalues)-1)-table[::-1].index(max(table))
        self.value=tiervalues[max([k for k in tiervalues.keys() if rarity>=k])]
tests=[]
mingems=[]
maxgems=[]
start=time.time()
for testno in range(1,10001):
    gems=[Gem().value for _ in range(10)]
    print("{}: {} {}".format(testno,sum(gems),str(gems)))
    if mingems and maxgems:
        if sum(gems)<min(tests):
            mingems=gems
        if sum(gems)>max(tests):
            maxgems=gems
    else:
        mingems=gems
        maxgems=gems
    tests.append(sum(gems))
elapsed=time.time()-start
print("Min: {} {}\nAverage: {}\nMedian: {}\nMax: {} {}\nStd Dev: {}\nSeconds taken: {}".format(min(tests),mingems,np.mean(tests),np.median(tests),max(tests),maxgems,np.std(tests),elapsed))
