# Russian Roulette
# NOT FINISHED YET!!!
import random

barrel = 5 * [''] + ['b']

def russian_roullete_part_one():
    print("\n\n\nRainy night, Calmness and Fireplace... So we're starting!")
    print("Welcome to Russian roulette,", end=" ")
    print("We have a revolver that has 6 bumps and in one of them - theres a BULLET!!!\n")
    person_1_name = input("Enter your name please    ")
    print(f"Welcome {person_1_name}. You're starting the game against Shahar Zori.")
    

    while True: 
        print("\n\n|MR. SHAHAR ZORI SHUFLING THE BARREL|\n\n")
        random.shuffle(barrel)
        shahar_zori = random.choice(barrel)
        if shahar_zori == 'b':
            print(f"Mr.Shahar Zori died. Today is your lucky night Mr. {person_1_name}. Go home.")
            break
        else:
            print(f"Lucky Shahar... Your turn Mr. {person_1_name}")
            while True:
                random.shuffle(barrel)
                person_1 = random.choice(barrel)
                if person_1 == 'b':
                    print(f"Goodbye Mr. {person_1_name}... Zori, Go home!")
                    break
                else:
                    print("Fucking lucky boy! SHAHAR, YOUR TURN!!!")
                    break


while True:
    user_prompt = input("Would you like to start the game?\nYes / No\n").strip().lower()
    
    if user_prompt == 'yes':
        russian_roullete_part_one()
        break
    elif user_prompt == 'no':
        print("\n\nOh, Have a Good night!")
        break
    else:
        print("\nWhat? Just enter 'Yes' or 'No'...\n")