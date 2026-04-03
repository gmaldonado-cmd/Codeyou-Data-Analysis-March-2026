
# Homework Game rock paper scissors
# create the imput random obtions  
import random   
options = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
print ("user_choice")

#Validate the user input
if user_choice not in options:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(options)
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
   
    # Determine the winner

if user_choice == computer_choice:
        print("Result: It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
        print("Result: You win! Rock beats scissors.")
elif user_choice == "paper" and computer_choice == "rock":
        print("Result: You win! Paper beats rock.")
elif user_choice == "scissors" and computer_choice == "paper":
        print("Result: You win! Scissors beat paper.")
else:
        print("Result: You lose! Computer wins.")
