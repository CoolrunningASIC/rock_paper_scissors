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

while running:
    challenge = None
    # generate random rock, paper, scissors
    guess = random.choice(valid_values[0:2])
    # prompt user to challenge computer to a valid game
    while challenge not in valid_values:
        challenge = input("Choose rock, paper, scissors, or quit: ").lower()
    if challenge == "quit":
        print("OK, bye")
        running = False
    else:
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

    print(f"{stats[0]} wins, and {stats[1]} losses and {stats[2]} ties,")