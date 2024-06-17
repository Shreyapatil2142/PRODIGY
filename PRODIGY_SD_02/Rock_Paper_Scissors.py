import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0

# Game logic
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    return result

def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"User Score: {user_score} - Computer Score: {computer_score}")

    if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
        user_choice_label.config(text="Your Choice: ")
        computer_choice_label.config(text="Computer's Choice: ")
        result_label.config(text="Result: ")
    else:
        root.quit()

# Create GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors")

instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
instructions.pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack()

rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: play("rock"))
rock_button.grid(row=0, column=0)

paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: play("paper"))
paper_button.grid(row=0, column=1)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: play("scissors"))
scissors_button.grid(row=0, column=2)

user_choice_label = tk.Label(root, text="Your Choice: ")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer's Choice: ")
computer_choice_label.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

score_label = tk.Label(root, text=f"User Score: {user_score} - Computer Score: {computer_score}")
score_label.pack()

root.mainloop()
