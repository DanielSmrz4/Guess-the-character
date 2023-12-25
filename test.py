import random

print("GUESS THE CHARACTER")

name_list = ["Jim", "Stifler", "Finch", "Ozz", "Kevin", "Mischelle", "Viki", "Sherminator"]
character = random.choice(name_list)
guess = ""
guess_count = 4

while guess != character:
    if guess_count != 0:
        guess = input("Zadejte jméno postavy z filmu American Pie: ")
        guess_count -= 1
    else:
        print("Out of tries, you LOOSE")
        break 
    if guess == character:
        print(f"YOU WIN! The character was {character}")
        break


