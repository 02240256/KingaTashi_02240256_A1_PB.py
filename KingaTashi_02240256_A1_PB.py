import random
while True:
    print("\nMenu:")
    print("1. Guess Number Game")
    print("2. Rock Paper Scisors Game ")
    print("Type 0 to EXIT")
    choice = input('Select Any Game : ').lower()
    if choice== "1":
        
        def guess_number_game():
            comp = random.randint(1,100)
            print(f"Welcome to guess number game.")
            print(f"guess a number from 1 to 100")
            
            while True :
                
                user_input = int(input("Enter your guess: "))
                if user_input < comp :
                    print("Guess Higher!! ")
                elif user_input > comp :
                    print("Guess Lower!! ")
                else:
                    print("CORRECT!!!")
                    choice = input("Do you want to play again?(y/n): ").lower()
                    if choice== "n": break
        guess_number_game()
    elif choice == "0":
        break
    else:
        
        def rock_paper_scissor():
            choices = ["rock", "paper", "scissor"]
            print("Welcome to Rock, Paper,Scissor Game!.")
            
            while True:
                user_input = input("Enter rock, paper, scissor: ").lower()
                computer_choice = random.choice(choices)
                print(f"computer choose:{computer_choice}")
                
            
                if user_input == computer_choice:
                    print("its a draw")
                elif (user_input == "rock" and computer_choice == "scissor") or \
                    (user_input == "paper" and computer_choice == "rock") or \
                    (user_input == "scissor" and computer_choice == "paper"):
                    print("VICTORY!:)")       
                else :
                    print("DEFEAT!:(")

                
                choose=input('Another Round? y/n : ').lower()
                if choose=='n': break
    
                    
            

        rock_paper_scissor() 
