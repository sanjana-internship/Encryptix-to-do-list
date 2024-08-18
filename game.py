import random
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    if choice in ["rock", "paper", "scissors"]:
        return choice
    else:
        print("Invalid choice. Try again.")
        return get_user_choice()

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
