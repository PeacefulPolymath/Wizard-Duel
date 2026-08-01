#Player
health = 100
shield = 2
attack = 3
heal = 1
xp = 0
#Monster
mhealth = 140
mattack = 5
#Basic UI
ui = '''#########################################
GAME BEGINS NOW
######################################### \n Note: Please choose options wisely. Failure in doing so would result in game getting ended\n'''
#Options
options = """ 1. Attack \n 2. Shield \n 3. Quit \n 4. Heal\n 5. Buy\n"""
#shop
shop = 'EVERYTHING COSTS 1 XP \n 1. +3 Attack\n 2. +2 Shield \n 3. +1 Heal \n 4. +4 Health \n 5.GO BACK\n'
print(ui)
while  mhealth > 0:
    #Stats
    print('Player Stats')
    print(f"Health: {health} \n Shield: {shield} \n Attack: {attack} \n Heal: {heal} \n XP: {xp} \n")
    print('Monster Stats')
    print(f'Health: {mhealth} \n Attack: {mattack}\n')
    print(options)
    option = int(input('Enter the option: '))
    if option > 5:
        print('Invalid Option!')
        break
    else:
        if option == 1:
            mhealth -= attack
            health -= mattack
            xp += 1
            print(f'You gave a damage of {attack}')
            print(f'Monster gave a damage of {mattack}')
        elif option == 2:
            mhealth -= attack/(4/shield)
            health -= mattack/(shield * 5)
            print(f'You gave a damage of {attack/(4/shield)} ')
            print(f'Monster gave a damage of {mattack/(5*shield)}')
        elif option == 3:
            print('Quitted!')
            break
        elif option == 4:
            if heal > 0:
                health += heal*5
                heal -= 1
                health -= mattack/2
            else:
                print('You dont have enough healing power!')
        elif option == 5 :
            if xp > 0:
                print(shop)
                shoption = int(input('Enter the option you want to choose: '))
                if shoption == 1:
                    attack += 3
                    xp -= 1
                elif shoption == 2:
                    shield += 2
                    xp -= 1
                elif shoption == 3:
                    heal += 1
                    xp -= 1
                elif shoption == 4:
                    health += 4
                    xp -= 1
                elif shoption == 5:
                    pass
                else:
                    print('Invalid option!')
                    break
            else:
                print('You dont have enough xp!')
    if health <= 0:
        break
print('Game Ended!')
                






