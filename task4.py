import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "User"
    else:
        return "Computer"

# Function to handle button click
def play(choice):
    global user_score, computer_score
    
    # Generate computer's choice based on difficulty level
    if difficulty.get() == "Easy":
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    elif difficulty.get() == "Medium":
        computer_choice = generate_medium_choice(choice)
    elif difficulty.get() == "Hard":
        computer_choice = generate_hard_choice(choice)
    
    winner = determine_winner(choice, computer_choice)
    
    if winner == "User":
        user_score += 1
        result_text = f"You win! ({choice} vs {computer_choice})"
    elif winner == "Computer":
        computer_score += 1
        result_text = f"You lose! ({choice} vs {computer_choice})"
    else:
        result_text = f"It's a tie! ({choice} vs {computer_choice})"
    
    # Update the result label
    label_result.config(text=result_text)
    label_score.config(text=f"Score - User: {user_score} | Computer: {computer_score}")

# Function to generate computer choice for medium difficulty
def generate_medium_choice(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    # Medium difficulty - More likely to counter the user's choice
    if user_choice == "Rock":
        return "Paper" if random.random() < 0.5 else random.choice(choices)
    elif user_choice == "Paper":
        return "Scissors" if random.random() < 0.5 else random.choice(choices)
    elif user_choice == "Scissors":
        return "Rock" if random.random() < 0.5 else random.choice(choices)

# Function to generate computer choice for hard difficulty
def generate_hard_choice(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    # Hard difficulty - Computer tries to win against the user’s choice
    if user_choice == "Rock":
        return "Paper"
    elif user_choice == "Paper":
        return "Scissors"
    elif user_choice == "Scissors":
        return "Rock"

# Function to ask if the user wants to play again
def play_again():
    response = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if response:
        # Reset the result label
        label_result.config(text="Choose Rock, Paper, or Scissors.")
    else:
        app.quit()

# Initialize scores
user_score = 0
computer_score = 0

# Create the main window
app = tk.Tk()
app.title("Rock, Paper, Scissors Game")

# Define colors
bg_color = '#f0f0f0'  # Light grey background
btn_color = '#4CAF50'  # Green background for buttons
text_color = '#000000'  # Black text color

# Set background color of the main window
app.configure(bg=bg_color)

# Define a larger font for widgets
large_font = ('Arial', 14)

# Instructions
label_instructions = tk.Label(app, text="Choose Rock, Paper, or Scissors:", font=large_font, bg=bg_color, fg=text_color)
label_instructions.pack(pady=10)

# Difficulty Level
label_difficulty = tk.Label(app, text="Choose Difficulty Level:", font=large_font, bg=bg_color, fg=text_color)
label_difficulty.pack(pady=10)
difficulty = tk.StringVar(value="Easy")  # Default value

radio_easy = tk.Radiobutton(app, text="Easy", variable=difficulty, value="Easy", font=large_font, bg=bg_color, fg=text_color, selectcolor=btn_color)
radio_easy.pack(pady=5)

radio_medium = tk.Radiobutton(app, text="Medium", variable=difficulty, value="Medium", font=large_font, bg=bg_color, fg=text_color, selectcolor=btn_color)
radio_medium.pack(pady=5)

radio_hard = tk.Radiobutton(app, text="Hard", variable=difficulty, value="Hard", font=large_font, bg=bg_color, fg=text_color, selectcolor=btn_color)
radio_hard.pack(pady=5)

# Buttons for choices
button_rock = tk.Button(app, text="Rock", command=lambda: play("Rock"), font=large_font, width=15, bg=btn_color, fg='white')
button_rock.pack(pady=5)

button_paper = tk.Button(app, text="Paper", command=lambda: play("Paper"), font=large_font, width=15, bg=btn_color, fg='white')
button_paper.pack(pady=5)

button_scissors = tk.Button(app, text="Scissors", command=lambda: play("Scissors"), font=large_font, width=15, bg=btn_color, fg='white')
button_scissors.pack(pady=5)

# Result Label
label_result = tk.Label(app, text="Choose Rock, Paper, or Scissors.", font=large_font, bg=bg_color, fg=text_color)
label_result.pack(pady=10)

# Score Label
label_score = tk.Label(app, text=f"Score - User: {user_score} | Computer: {computer_score}", font=large_font, bg=bg_color, fg=text_color)
label_score.pack(pady=10)

# Play Again Button
button_play_again = tk.Button(app, text="Play Again", command=play_again, font=large_font, width=15, bg=btn_color, fg='white')
button_play_again.pack(pady=10)

# Run the main event loop
app.mainloop()
