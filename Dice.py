from random import choice

Input = input("Type \Roll/ to roll the dice: ")
dice = [1,2,3,4,5,6]
roll = choice(dice)

if  roll <= 3 and Input == "Roll":
    print(f"Dice: ", roll , " Unlucky")
elif roll >= 6 and Input == "Roll":
    print(f"Dice: ", roll , " Very lucky")
    
