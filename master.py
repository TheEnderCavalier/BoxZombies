import random
import numpy as np
class Gem:
    name=""
    rarity=0
    value=0
    def __init__(self):
        tiervalues={0:random.randint(1,1000000),0.5:random.randint(10,1000000),
        0.75:random.randint(100,1000000),0.875:random.randint(1000,1000000),
        0.9375:random.randint(10000,1000000),0.96875:random.randint(100000,1000000),
        0.984375:random.randint(1000000,10000000)}
        self.name="".join([random.choice("qwertyuiopasdfghjklzxcvbnm") for x in range(random.randint(2,10))]).capitalize()
        rarity=random.random()
        table=[rarity>=x for x in tiervalues.keys()]
        self.rarity=(len(tiervalues)-1)-table[::-1].index(max(table))
        self.value=tiervalues[max([k for k in tiervalues.keys() if rarity>=k])]
    def unveil(self):
        print("A gem of {0} with rarity {1} valued at {2}".format(self.name,self.rarity,self.value))
tests=[]
mingems=[]
maxgems=[]
for testno in range(100000):
    gems=[Gem().value for _ in range(10)]
    print("{}: {} ({})".format(testno,sum(gems),str(gems)))
    if mingems and maxgems:
        if sum(gems)<min(tests):
            mingems=gems
        if sum(gems)>max(tests):
            maxgems=gems
    else:
        mingems=gems
        maxgems=gems
    tests.append(sum(gems))
tests=tests[1:]
print("Min: {} ({})\nAverage: {}\nMedian: {}\nMax: {} ({})\nStd Dev: {}".format(min(tests),mingems,np.mean(tests),np.median(tests),max(tests),maxgems,np.std(tests)))
