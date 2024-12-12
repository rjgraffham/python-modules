import argparse
import random

def main(min_secret, max_secret):
    secret_number = random.randint(min_secret, max_secret)

    guess_count = 0

    print(f"I'm thinking of a secret number no less than {min_secret} and no more than {max_secret}.")

    while True:
        guess = input(f"\nEnter your guess ({min_secret}-{max_secret}, or 0 to exit game): ").strip()

        try:
            guess = int(guess)
        except ValueError:
            print("Guess must be a number.")
            continue

        if guess == 0:
            print("Bye!")
            break

        if guess < min_secret or guess > max_secret:
            print(f"Guess must be between {min_secret} and {max_secret}.")
            continue

        # if we got past the validity checking, this is a valid guess, increment the guess count
        guess_count += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        elif guess_count == 1:  # implicitly the guess is correct if it was neither lower or higher
            print(f"Got it in one! The secret number was {secret_number}.")
            break
        else:
            print(f"Well done! The secret number was {secret_number}. You got it in {guess_count} guesses.")
            break
    
    print() # print a final blank line to separate the last message from the next command prompt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Number Guessing Game")
    parser.add_argument("-m", "--min", type=int, default=1, help="Minimum secret number (no less than 1)")
    parser.add_argument("-x", "--max", type=int, default=100, help="Maximum secret number")
    args = parser.parse_args()

    if args.min < 1:
        print("Minimum secret number must not be less than 1.")
    if args.max < args.min:
        print("Maximum secret number must not be less than minimum secret number.")
    else:
        try:
            main(args.min, args.max)
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
        except Exception as e:
            print(f"Unexpected exception {type(e)}: {e}")