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
# v1.4.2.1: Today I did a patch that doesn't break the game from someone else's house.
from random import randint
import time
print "TheEnderCavalier presents..."
time.sleep(3)
print "From Brad Sparks' classroom..."
time.sleep(3)
print "BOX: ZOMBIE EDITION"
time.sleep(3)
print "v1.4.2.1"
time.sleep(3)
print "Each wave, you open the box."
print "The box gives you gems, which you use to buy ammo."
print "Then zombies come and try to kill you."
print "You one-tap them, and if you can one-tap them all, you survive."
print "Somehow getting an everstone buys you an grenade which can waveclear."
print "Try to survive a lot of waves for a high score!"
time.sleep(10)
ammotot=0
wave=0
alive=True
boss=10
ammo2=1
chance2=1
while alive==True:
    wave+=1
    print "Wave", wave
    if chance2>1 or ammo2>1:
        time.sleep(2)
        print "Perks:"
        if ammo2>1:
            print "Ammo+ lv", ammo2
        if chance2>1:
            print "Chance+ lv", chance2
    time.sleep(3)
    x=0
    perk=0
    boss2=0
    grenade=0
    topaz=0
    sapphire=0
    amethyst=0
    ruby=0
    emerald=0
    diamond=0
    everstone=0
    rare=0
    bosskill=0
    chance=0
    print "The box opens."
    time.sleep(1)
    while x<10:
        tiernum=randint(1,((499*(chance2))+(wave*(chance2*2))))
        tier=0
        if tiernum>=4000:
            tier=7
        elif tiernum>=1000:
            tier=6
            rare=1
        elif tiernum>=500:
            tier=5
            rare=1
        elif tiernum>=450:
            tier=4
            rare=1
        elif tiernum>=400:
            tier=3
            rare=1
        elif tiernum>=350:
            tier=2
            rare=1
        else:
            if rare==0 and x==9:
                tiernum=randint(0,100)
                if tiernum>=100:
                    tier=5
                    rare=1
                elif tiernum>=98:
                    tier=4
                    rare=1
                elif tiernum>=95:
                    tier=3
                    rare=1
                else:
                    tier=2
                    rare=1
            else:
                tier=1
        if tier==7:
            print "EVERSTONE!!! +100 points"
            everstone+=1
        elif tier==6:   
            print "DIAMOND! +75 points"
            diamond+=1
        elif tier==5:
            print "Emerald! +50 points"
            emerald+=1
        elif tier==4:
            print "Ruby! +20 points"
            ruby+=1
        elif tier==3:
            print "Amethyst. +10 points"
            amethyst+=1
        elif tier==2:
            print "Sapphire. +5 points"
            sapphire+=1
        else:
            print "Topaz... +1 point"
            topaz+=1
        x+=1
        time.sleep(0.1)
    print "Converting all into topaz..."
    time.sleep(2)
    topaz+=(100*everstone)+(75*diamond)+(50*emerald)+(20*ruby)+(10*amethyst)+(5*sapphire)
    print "Final worth:", topaz
    ammo=topaz*int((randint(800,(1300*ammo2))/100.0))
    time.sleep(1)
    print "By selling each topaz you gained", ammo, "ammo."
    time.sleep(1)
    ammotot+=ammo
    print "You now have", ammotot, "ammo for your pistol."
    if everstone>=1:
        print "One arms dealer gives you a grenade which should take out a well-sized cluster."
        grenade=(randint(150,250))*2
        ammotot+=grenade
    time.sleep(2)
    print "Zombies are closing in on your location!"
    time.sleep(2)
    zombie=int(((randint(500,2000)/10.0)*(wave)))
    print "On closer inspection, you see that", zombie, "zombies have appeared."
    time.sleep(2)
    if ammotot>=zombie:
        print "You have successfully countered the horde!"
        ammotot-=grenade
        ammotot-=zombie-grenade
        zombie=0
        if ammotot<0:
            ammotot=0
        time.sleep(1)
        if wave-boss==0:
            time.sleep(2)
            boss+=1
            print "Out of the smoke, a boss appears!"
            time.sleep(3)
            boss2=randint(1,1)
            if boss2==1:
                print "It's eyes glow red in a fury and it charges at you."
                time.sleep(2)
                if grenade>1:
                    print "You throw your grenade."
                    time.sleep(4)
                    chance=randint(1,10)
                    if chance>=3:
                        print "The boss is obliberated by the blast."
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
