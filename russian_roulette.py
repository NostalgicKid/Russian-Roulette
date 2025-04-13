# Russian Roulette
# NOT FINISHED YET!!!
import random

user_prompt = input("Would you like to start the game?\nYes / No\n")


barell = 5 * [''] + ['b']


person_name_1 = input("E")
 
def russian_roullete_part_one():
    print("\n\n\nRainy night, Calmness and Fireplace... So we're starting!\n")
    print("Welcome to Russian roulette,", end="")
    print("We have a revolver that has 6 bumps and in one of them - theres a BULLET!!!")
    
    while person_1 or person_2 not in ['b']:
        random.shuffle(barell)
        person_1 = random.choice()
if user_prompt == 'yes':
    print(ru ss ian_roullete_part_one())
else:
    user_prompt = input("What? Enter Yes or No! ") 
    while user_prompt.lower() not in ('yes', 'no'):
        user_prompt = "What..? again, Enter 'Yes' or 'No'."
    if user_prompt.lower() == 'yes':
        print(russian_roullete_part_one())
    else:
        print('GoodBye Dear, Have a nice rainy night!')
