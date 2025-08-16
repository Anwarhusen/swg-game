import random

def get_user_choice():
    """Get and validate user input with error handling"""
    while True:
        try:
            usr = int(input("Enter 1 for Snake, 2 for Water, 3 for Gun: "))
            if usr in [1, 2, 3]:
                return usr
            else:
                print("Invalid input! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def determine_winner(user, computer):
    """Determine the winner based on game rules"""
    if user == computer:
        return "draw"
    elif (user == 1 and computer == 2) or \
         (user == 2 and computer == 3) or \
         (user == 3 and computer == 1):
        return "user"
    else:
        return "computer"

def play_game():
    """Main game function with score tracking"""
    user_score = 0
    computer_score = 0
    rounds = 0
    
    option = {1: "Snake", 2: "Water", 3: "Gun"}
    
    while True:
        rounds += 1
        print(f"\nRound {rounds}")
        print(f"Current Score - You: {user_score}, Computer: {computer_score}")
        
        usr = get_user_choice()
        cmp = random.randint(1, 3)
        
        print(f"\nYour choice: {option[usr]}")
        print(f"Computer's choice: {option[cmp]}")
        
        result = determine_winner(usr, cmp)
        
        if result == "draw":
            print("It's a draw!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nFinal Score:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You won the game!")
            elif computer_score > user_score:
                print("Computer won the game. Better luck next time!")
            else:
                print("The game ended in a tie!")
            break

if __name__ == "__main__":
    print("Welcome to Snake-Water-Gun Game!")
    print("Game Rules:")
    print("- Snake (1) beats Water (2)")
    print("- Water (2) beats Gun (3)")
    print("- Gun (3) beats Snake (1)")
    play_game()

