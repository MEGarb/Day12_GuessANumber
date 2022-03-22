import random

def set_difficulty():
    difficulty = input("\nWhat difficulty would you like to play on? 'easy' or 'hard'  ").lower()
    if  difficulty == 'easy':
        chances = 10
    elif difficulty == 'hard':
        chances = 5
    else:
        print("Invalid entry in set_difficulty")
        quit()
    print ("")

    return chances

def feedback(tar, curr, play):
    if tar == curr:
        print(f"You have guessed {curr} the secret number is {tar}.")
        print("You have guessed correctly.  You win!\n")
        play = False

    elif tar > curr:
        print(f"You have guessed {curr}")
        print("Your guess is low\n")

    elif tar < curr:
        print(f"You have guessed {curr}")
        print("Your guess is high\n")

    return play


play_game = True

while play_game:
    guesses_remaining = set_difficulty()
    target_num = random.randint(1, 100)

    game_status = True
    while game_status and guesses_remaining > 0:
        print("\nGuess a number between 1 and 100.")
        curr_guess = int(input("Please enter your guess:  "))
        print("")

        game_status = feedback(target_num, curr_guess, game_status)
        guesses_remaining -= 1


    if guesses_remaining == 0:
        print(f"You have run out of guesses.  The secret number was {target_num}\n")

    if input("Would you like to play again?  'y' or 'n'").lower() == 'n':
        play_game = False
