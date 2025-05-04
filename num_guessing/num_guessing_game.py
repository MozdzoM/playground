from random import randint


EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_DIFFICULTY
    elif difficulty == "hard":
        return HARD_DIFFICULTY

print("Welcome to a Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
# print(f"Psst! the number is: {answer}")

attempts = set_difficulty()

is_game_over = False
while not is_game_over:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1

    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        break
    elif guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")

    if attempts > 0:
        print("Guess again.")
    else:
        print("You've run out of guesses, you lose.")
        is_game_over = True
