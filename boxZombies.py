# BOX: ZOMBIE EDITION
# By TheEnderCavalier
# v1.0: Release.
# v1.1: Made ammo gain more random to make high scores easier.
# Statistically, the game is still the same difficulty.
# It's also harder to get higher valued gems, but the probability goes up
# with the wave instead of down.
# Also changed how the random gen for ammo and zombies works to be more random.
# v1.2: Made it possible for more zombies to appear.
# Also imported the highscore thing from legoMan's patch.
# Added a grenade and airstrike as well.
# v1.2.1: Fixed a bug where using the grenade can lead to negative ammo.
# v1.2.1.1: Fixed another bug with the grenade.
# v1.3: Added the amethyst and upped the value of the rest of the gems.
# Also removed the airstrike due to NEVER WORKING.
# Less zombies can appear, but a boss can appear to counter that.
# There is only one boss, which has a chance to be insta'd with a grenade and/or 1000 bullets.
# v1.3.1: Changed how bosses spawn.
# Also made the late-game easier.
# v1.4: Wow! A major update right after a patch!
# Added two perks that can majorly affect gameplay upon attaining.
# There isn't much difference between them.
# They are Chance+ (much higher gem gain) and Ammo+ (much higher ammo gain).
# These are designed to make the game a bit more interactive and much easier.
# v1.4.1: Fixed a crash that killed everything.
# v1.4.1.1: Made the red boss weaker and not impossible to kill consistently.
# v1.4.1.2: Made the everstone unattainable without insane waveclear or perks.
# v1.4.2: A bit of rebalancing and ANOTHER bugfix. Also, in game instructions.
# Highscore function removed until online save exists.
# I hope I can make this a .exe and .app file soon.
# Diamond now requires a perk.
# v1.4.2.1: Added two perks (Damage+ and Power+).
# They are currently unattainable, but will be from the planned blue boss.
# Today, I'm really lazy to design.
# v1.4.2.2: Fixed a bug with the ammo value and nerfed ammo gain.
# v1.4.2.2.1: No bugfixes, just a nerf in ammo gain.
# v1.5: I MADE ANOTHER BUSSES
# HAZ PUN
# v1.5.1: Re-balancing, blue boss bugfix.
# Mainly, increase in gem price.
# The onyx gem has been introduced as +1. Topaz is now +3, but can still give last box.
# v1.5.1.1: Bugfixes, and what I forgot in rebalancing.
# v1.6: Added the bloodstone due to a coding error. Also, to make it fair, hella rebalancing.
from random import randint
import time
print "TheEnderCavalier presents..."
time.sleep(3)
print "From Brad Sparks' classroom..."
time.sleep(3)
print "BOX: ZOMBIE EDITION"
time.sleep(3)
print "v1.6"
time.sleep(3)
print "Each wave, you open the box."
time.sleep(0.5)
print "The box gives you gems, which you use to buy ammo."
time.sleep(0.5)
print "Then zombies come and try to kill you."
time.sleep(0.5)
print "You one-tap them, and if you can one-tap them all, you survive."
time.sleep(0.5)
print "Somehow getting an everstone buys you an grenade which can waveclear."
time.sleep(0.5)
print "Try to survive a lot of waves for a high score!"
time.sleep(2.5)
ammotot=0
wave=0
alive=True
ammo2=1
chance2=1
damage2=1
power2=1
boss=0
while alive==True:
    wave+=1
    print "Wave", wave
    if chance2>1 or ammo2>1 or damage2>1 or power2>1:
        time.sleep(2)
        print "Perks:"
        if ammo2>1:
            print "Ammo+ lv", ammo2
        if chance2>1:
            print "Chance+ lv", chance2
        if damage2>1:
            print "Damage+ lv", damage2
        if power2>1:
            print "Power+ lv", power2
    time.sleep(3)
    clash=0
    x=0
    killvalue=0
    hp=100
    chancechance=0
    chancechancechance=0
    perk=0
    boss2=0
    grenade=0
    topaz=0
    sapphire=0
    bloodstone=0
    amethyst=0
    ruby=0
    emerald=0
    diamond=0
    everstone=0
    rare=0
    bosskill=0
    chance=0
    onyx=0
    gungungungungun="your pistol."
    print "The box opens."
    time.sleep(1)
    while x<10:
        tiernum=randint(1,((399*(chance2))+(wave*(chance2*2))))
        tier=0
        if tiernum>=4000:
            tier=8
        elif tiernum>=1000:
            tier=7
            rare=1
        elif tiernum>=500:
            tier=6
            rare=1
        elif tiernum>=400:
            tier=5
            rare=1
        elif tiernum>=300:
            tier=4
            rare=1
        elif tiernum>=200:
            tier=3
            rare=1
        elif tiernum>=100:
            tier=2
        elif tiernum>=10:
            if rare==0 and x==9:
                tiernum=randint(0,100)
                if tiernum>=100:
                    tier=6
                    rare=1
                elif tiernum>=98:
                    tier=5
                    rare=1
                elif tiernum>=95:
                    tier=4
                    rare=1
                else:
                    tier=3
                    rare=1
            else:
                tier=1
        else:
            tier=0
        if tier==8:
            print "EVERSTONE!!! +1000 POINTS"
            everstone+=1
        elif tier==7:
            print "DIAMOND! +150 points"
            diamond+=1
        elif tier==6:
            print "Emerald! +75 points"
            emerald+=1
        elif tier==5:
            print "Ruby! +25 points"
            ruby+=1
        elif tier==4:
            print "Amethyst. +15 points"
            amethyst+=1
        elif tier==3:
            print "Sapphire. +7 points"
            sapphire+=1
        elif tier==2:
            print "Topaz... +3 points"
            topaz+=1
        elif tier==1:
            print "Onyx... +1 point"
            onyx+=1
        else:
            print "It was a bloodstone. -50 points"
            bloodstone-=1
        x+=1
        time.sleep(0.1)
    print "Converting all into onyx..."
    time.sleep(2)
    onyx+=(1000*everstone)+(150*diamond)+(75*emerald)+(25*ruby)+(15*amethyst)+(7*sapphire)+(3*topaz)-(50*bloodstone)
    print "Final worth:", onyx
    ammo=onyx*int((randint(750,(1125*ammo2))/100.0))
    time.sleep(1)
    print "By selling each topaz you gained", ammo, "ammo."
    time.sleep(1)
    ammotot+=ammo
    if ammotot>=1000000000:
        gungungungungun="the insane contraption you have built out of 36 miniguns which mauls anything in your path."
        grenade = (randint(500, 1000)) * power2
        ammotot += grenade
    elif ammotot>=30000:
        gungungungungun="your minigun."
    elif ammotot>=15000:
        gungungungungun="your heavy machine gun."
    elif ammotot>=5000:
        gungungungungun="your assault rifle."
    elif ammotot>=1000:
        gungungungungun="your SMG."
    else:
        gungungungungun="your pistol."
    print "You now have", ammotot, "ammo for", gungungungungun
    if everstone>=1:
        print everstone, "arms dealer(s) give(s) you a grenade which should take out a well-sized cluster."
        grenade=(randint(500,1000))*power2*everstone
        ammotot+=grenade
    time.sleep(2)
    print "Zombies are closing in on your location!"
    time.sleep(2)
    zombie=int(((randint(750,2250)/10.0)*(wave))/(damage2))
    print "On closer inspection, you see that", (zombie*damage2), "zombies have appeared."
    time.sleep(2)
    if ammotot>=zombie:
        print "You have successfully countered the horde!"
        ammotot-=grenade
        ammotot-=zombie-grenade
        zombie=0
        if ammotot<0:
            ammotot=0
        time.sleep(1)
        if wave%10==0:
            time.sleep(2)
            boss+=1
            print "Out of the smoke, a boss appears!"
            time.sleep(3)
            boss2=randint(1,2)
            if boss2==1:
                print "Its eyes glow red in a fury and it charges at you."
                time.sleep(2)
                if grenade>1:
                    print "You throw your grenade."
                    time.sleep(4)
                    chance=randint(1,10)
                    if chance>=3:
                        print "The boss is obliterated by the blast."
                        bosskill=1
                        time.sleep(1)
                    else:
                        print "It explodes, but the boss shrugs it off."
                time.sleep(2)
                if bosskill==0 and ammotot>=500:
                    print "You shoot 500 bullets into its forehead."
                    time.sleep(2)
                    print "The boss is shot down and falls with a thump."
                    bosskill=1
                    time.sleep(2)
                if bosskill==1:
                    print "A winner is you!"
                    boss+=10
                    time.sleep(2)
                    print "You take a crystal out of its back, which makes you feel stronger."
                    time.sleep(2)
                    while True:
                        print "1: Ammo+"
                        print "2: Chance+"
                        if ammo2<=1 or chance2<=1:
                            print "Tip: Ammo+ is a direct increase to your stash, great for mid and late game (wave 30-40)."
                            print "Chance+ does you good till lv 3, where you should start going Ammo+ until wave 100 (or wave 50 if you want to go everstone hunting."
                        perk=raw_input("Choice: ")
                        if perk=="1" or perk=="2":
                            if perk=="1":
                                print "It makes you feel like a better bargainer."
                                ammo2+=1
                                time.sleep(2)
                                break
                            else:
                                print "It makes you feel luckier. The box feels heavier."
                                chance2+=1
                                time.sleep(2)
                                break
                        else:
                            perk=0
                if ammotot<500:
                    print "The boss slaps you aside, effectively killing you."
                    time.sleep(1)
                    print "Your dead body is found with", ammotot, "bullets to spare."
                    ammo=0
                    alive=False
            elif boss2==2:
                print "Its eyes glow blue. He takes out a pistol, somehow."
                time.sleep(2)
                while clash==0:
                    print "You both empty a clip."
                    ammo-=30
                    time.sleep(0.25)
                    chancechance=randint(1,100)
                    if chancechance>=99:
                        print "You kill it with a good headshot."
                        time.sleep(2)
                        bosskill=1
                        clash=1
                    elif chancechance>=40:
                        chancechancechance=randint(100,3000)/100
                        killvalue=3*chancechancechance
                        hp-=killvalue
                        print "You hit it", killvalue/3, "times."
                        time.sleep(0.25)
                        if hp<=0:
                            break
                    elif chancechance>=15:
                        print "Your aim fails you."
                        time.sleep(0.25)
                    else:
                        print "Your aim fails you."
                        time.sleep(0.25)
                        print "And you die."
                        time.sleep(1.75)
                        time.sleep(1)
                        print "Your dead body is found with", ammotot, "bullets to spare."
                        ammo=0
                        alive=False
                        clash=1
                if bosskill==1:
                    print "A winner is you!"
                    boss+=10
                    time.sleep(2)
                    print "You take a amulet of pure crystal of its neck. You feel an increase in power."
                    time.sleep(2)
                    while True:
                        print "3: Damage+"
                        print "4: Power+"
                        if ammo2<=1 or chance2<=1:
                            print "Tip: Damage+ should be the way to go unless you can get wave 200+, in which case you should max Chance+ and Power+ and depend on the surplus of grenades."
                        perk=raw_input("Choice: ")
                        if perk=="3" or perk=="4":
                            if perk=="3":
                                print "Your aim improves. You near a constant bullseye."
                                damage2+=1
                                time.sleep(2)
                                break
                            else:
                                print "The intensity of anything that touches you increases."
                                power2+=1
                                time.sleep(2)
                                break
                        else:
                            perk=0
        if alive==True:
            print "You have", ammotot, "ammo left."
    else:
        print "The zombies have mauled you with their numbers."
        ammotot-=grenade
        ammotot-=zombie/2
        if ammotot<0:
            ammotot=0
        time.sleep(1)
        print "Your dead body is found with", ammotot, "bullets to spare."
        ammo=0
        alive=False
    time.sleep(3)
print "GAME OVER"
print "Score: ", wave-1
