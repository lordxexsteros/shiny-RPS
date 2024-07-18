import random

def get_user_choice():
    # Function to get user's choice
    choices = ['rock', 'paper', 'scissors']
    while True:
        print("\n--- Rock, Paper, Scissors ---")
        print("Enter your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Your choice (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return choices[int(choice) - 1]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_computer_choice():
    # Function to get computer's choice
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Function to determine the winner
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing Rock, Paper, Scissors!")

# Run the game
play_game()
