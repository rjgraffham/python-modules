import argparse
import random
from tkinter import Tk, StringVar, ttk

### TODO: make an object to attach state to instead of passing it around
### TODO: further to the above - break out the guessing logic (state, messages,
###       etc.) to a class that can be instantiated by any of the three programs
###       so that they can share improvements to that. of note, this means the
###       responses should be able to distinguish between "this is an error",
###       "this is a response to an incorrect guess", and "this is a response
###       to a correct guess", as those may be displayed differently (e.g.,
###       the CLI guesser ends on a correct guess, prompts again on an error,
###       or simply displays higher/lower on an incorrect guess)
### TODO: make the output a scrollable label instead of replacing
### TODO: scroll to the bottom of the label every time it's added to
### TODO: do not allow pressing Return in the entry when it's disabled
### TODO: make the scrollable label resize to fill, so the UI always fills
###       the whole window
### TODO: look into whether the font can scale up as the window gets larger?
### TODO: add an initial window to prompt for the min and max if not passed in
### TODO: add a button to recall the min/max window (should reset the game if
###       min or max changes)

def make_guess_evaluator(min_secret, max_secret, guess_var, guess_entry, msg_label, guess_btn):
    secret_number = random.randint(min_secret, max_secret)
    msg_label["text"] = f"I'm thinking of a secret number no less than {min_secret:,} and no more than {max_secret:,}."
    guess_count = 0
    playing = True

    def guess_evaluator(*_args):
        nonlocal secret_number, guess_count, playing

        # if already completed, the button is now a play again button
        if not playing:
            secret_number = random.randint(min_secret, max_secret)
            msg_label["text"] = f"I'm thinking of a new secret number no less than {min_secret:,} and no more than {max_secret:,}."
            guess_btn["text"] = "Guess"
            guess_count = 0
            guess_entry.config(state="enabled")
            playing = True
            return
        
        guess = guess_var.get()

        try:
            guess = int(guess.replace(",", "").replace(" ", ""))
        except ValueError:
            msg_label["text"] = "Guess must be a number."
            return

        if guess < min_secret or guess > max_secret:
            msg_label["text"] = f"Guess must be between {min_secret:,} and {max_secret:,}."
            return

        # if we got past the validity checking, this is a valid guess, increment the guess count
        guess_count += 1

        if guess < secret_number:
            msg_label["text"] = f"{guess:,} is too low!"
        elif guess > secret_number:
            msg_label["text"] = f"{guess:,} is too high!"
        elif guess_count == 1:  # implicitly the guess is correct if it was neither lower or higher
            msg_label["text"] = f"Got it in one! The secret number was {secret_number:,}."
            guess_btn["text"] = "Play again!"
            guess_var.set("")
            guess_entry.config(state="disabled")
            playing = False
        else:
            msg_label["text"] = f"Well done! The secret number was {secret_number:,}. You got it in {guess_count:,} guesses."
            guess_btn["text"] = "Play again!"
            guess_var.set("")
            guess_entry.config(state="disabled")
            playing = False
        
    return guess_evaluator

def main(min_secret, max_secret):
    app = Tk()
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.title("Guessing Game")
    app.geometry("840x180")
    frame = ttk.Frame(app, padding = 10)
    frame.grid(column=0, row=0, sticky="NESW")
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1)
    frame.grid_rowconfigure(2)
    frame.grid_rowconfigure(3, weight=1)
    msg_label = ttk.Label(frame, font=("Segoe UI", 16, "bold"))
    msg_label.grid(column=0, row=0, sticky="S")
    ttk.Label(frame, text=f"Enter your guess ({min_secret:,}-{max_secret:,}):", font=("Segoe UI", 16, "")).grid(column=0, row=1)
    guess_var = StringVar()
    guess_entry = ttk.Entry(frame, textvariable=guess_var, font=("Segoe UI", 16, ""))
    guess_entry.grid(column=0, row=2)
    guess_btn = ttk.Button(frame, text="Guess")
    guess_btn.grid(column=0, row=3, sticky="N")
    guess_evaluator = make_guess_evaluator(min_secret, max_secret, guess_var, guess_entry, msg_label, guess_btn)
    guess_entry.bind("<Key-Return>", guess_evaluator)
    guess_btn["command"] = guess_evaluator
    app.mainloop()

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