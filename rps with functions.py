import random
valid_values = ("rock", "paper", "scissors", "quit")
# stats are win. lose, draw
stats = [0,0,0]
victories = [
    ["paper", "rock"],
    ["rock", "scissors"],
    ["scissors", "paper"]
    ]
running = True

def get_user_selection():
    # prompt user to challenge computer to a valid game
    challenge = None
    while challenge not in valid_values:
        challenge = input("Choose rock, paper, scissors, or quit: ").lower()
    return challenge

def get_computer_selection():
    # generate random rock, paper, scissors
    guess = random.choice(valid_values[0:2])
    return guess

def determine_winner(challenge, guess):
    # determine winner and display result
    if challenge == guess:
        stats[2] += 1
        print("Tie! Try again")
    elif [challenge, guess] in victories:
        stats[0] += 1
        print(f"The {challenge} beats the {guess}, you win!")
    else:
        stats[1] += 1
        print(f"The {guess} beats the {challenge}, you lose!")

while running:
    challenge = get_user_selection()
    guess = get_computer_selection()
    if challenge == "quit":
        print("OK, bye")
        running = False
    else:
        determine_winner(challenge, guess)
    print(f"{stats[0]} wins, and {stats[1]} losses and {stats[2]} ties,")