import time
import random
print("это игра на выживание")
time.sleep(2)
print('Ты в могазине купил 3 бутылки Fanta с разными вкусами')
time.sleep(1)
print('1 --> клубника')
print('2 --> черника')
print('3 --> лимон')
time.sleep(1)

play = int(input('выбери вкус;'))
if play == 1:
    print('ты попал в брошенное здание и перед тобой 2 двери ')
    time.sleep(1)
    print('1 деревянная дверь')
    print('2 стальнаядверь')

    play2 = int(input('выбери дверь; '))
    time.sleep(1)
    if play2 == 1:
        print('ты попал в каменный век, тебе придется жить там до самой смерти ')
    elif play2 == 2:
        print(' ты попал эпоху динозавров и тебя съели...')
elif play == 2:
    print('ты попал в 1812 год, и тебя забрали на войну ')

elif play == 3:
    print('ты попал в космос и перед тобой 4 партала ')
    print('1 черный ')
    print('2 зелёный')
    print('3 синий')
    print('4 белый')
    play3 = int(input('выбери портал;'))
    if play3 == 1:
        print('ты оказался внутри охваченного огнём дома')
        a = random.randint(1,5)
        if a == 3:
            print('ты выбрался из этого дома')
        else:
            print('ты сгорел вместе с домом')
    elif play3 == 2:
        print('ты оказал посередине Атлантического окена')
        b = random.randint(10)
        if b == 0:
            print(" ты утонул")
        elif b == 5:
            print('тебя спасли')
        else:
            print('тебя скушали акулы')
    elif play3 == 3:
        print('ты превротился в чернику')
    elif play3 == 4:
        print('все это оказалось сном даже то что ты купил Fantу, ты проснулся ')
print('Game Over')