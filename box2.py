import random
class Gem:
    name=""
    rarity=0
    value=0.0
    tiervalues={0:random.randint(0,1000)/100,0.5:random.randint(1000,10000)/100,0.75,0.875,0.9375,0.96875}
    def __init__(self):
        self.name="".join([random.choice("qwertyuiopasdfghjklzxcvbnm") for x in range(random.randint(4,16))]).capitalize()
        rarity=random.random()
        self.rarity=(len(self.tiernames)-1)-[rarity>=x for x in self.tiernames.keys()][::-1].index(max(rarity))

    def unveil(self):
        pass
Gem()
