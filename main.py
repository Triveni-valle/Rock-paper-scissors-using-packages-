import random
choices = ["rock", "paper", "scissors"]
def get_computer_choice():
    return random.choice(choices)
def check_winner(player, computer):
    if player == computer:
        return "Draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You Win"
    else:
        return "Computer Wins"
def play_game():
    print(" Rock Paper Scissors Game")

    while True:
        player = input("Enter rock, paper, scissors (or quit): ").lower()

        if player == "quit":
            print("Game Over!")
            break

        if player not in choices:
            print("Invalid input! Try again.")
            continue

        computer = get_computer_choice()

        print("You:", player)
        print("Computer:", computer)

        result = check_winner(player, computer)
        print("Result:", result)
        print("-" * 25)
if __name__ == "__main__":
    play_game()
