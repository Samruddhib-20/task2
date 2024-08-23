import random
def main():
    user_action = input("Enter a choice(Rock, Paper, Scissors):")
    pos_action = ["Rock", "Paper", "Scissors"]

    computer_action = random.choice(pos_action)
    print(f"\n You choose {user_action}, computer choose {computer_action}")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! you win!")
        else:
            print("Paper covers rock! You lose.")
        
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose.")
        
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissor cuts Paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
        
if __name__ == "__main__":
    main()