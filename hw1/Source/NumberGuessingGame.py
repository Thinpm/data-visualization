import tkinter as tk
from tkinter import messagebox
import random
import os
import csv

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.configure(bg="#f0f8ff")  # Set background color for the window
        
        # Initialize variables
        self.secret_number = None
        self.attempts = 0
        self.current_guesses = []
        self.game_count = 1
        self.history_file = "history.csv"  # File to store the history
        self.player_name = ""  # Store player's name
        
        # Create history file if it doesn't exist
        if not os.path.exists(self.history_file):
            with open(self.history_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Player Name", "Secret Number", "Guessed Numbers", "Attempts"])  # Column headers

        # Create the user interface
        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="What's Your Lucky Number?", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#00008b")
        self.title_label.pack(pady=10)

        # Instructions
        self.instruction_label = tk.Label(self.root, text="Guess a number between 1 and 1000!")
        self.instruction_label.pack()

        # Player's name input and "Start Game" button
        self.name_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.name_frame.pack(pady=5)

        self.name_label = tk.Label(self.name_frame, text="Enter player's name:", bg="#f0f8ff", fg="#00008b")
        self.name_label.pack(side=tk.LEFT, padx=5)
        self.name_entry = tk.Entry(self.name_frame, font=("Arial", 14), bg="#fff", fg="#00008b", bd=2)
        self.name_entry.pack(side=tk.LEFT, padx=5)

        self.start_button = tk.Button(self.name_frame, text="Start Game", command=self.start_game, bg="#32cd32", fg="white", font=("Arial", 14), bd=3, activebackground="#98fb98")
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Hint
        self.hint_label = tk.Label(self.root, text="Hint will appear here.", font=("Arial", 24, "italic"), bg="#f0f8ff", fg="#ff6347")
        self.hint_label.pack(pady=10)

        # Guess input
        self.input_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.input_frame.pack(pady=10)

        self.guess_entry = tk.Entry(self.input_frame, font=("Arial", 14), bg="#fff", fg="#00008b", bd=2)
        self.guess_entry.pack(side=tk.LEFT, padx=5)

        # Bind Enter key event
        self.guess_entry.bind("<Return>", self.check_guess_event)

        self.guess_button = tk.Button(self.input_frame, text="Guess", command=self.check_guess, bg="#4682b4", fg="white", font=("Arial", 14), bd=3, activebackground="#5f9ea0")
        self.guess_button.pack(side=tk.LEFT, padx=5)

        # Control buttons
        self.control_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.control_frame.pack(pady=10)

        self.quit_button = tk.Button(self.control_frame, text="Exit", command=self.root.quit, bg="#ff6347", fg="white", font=("Arial", 14), bd=3, activebackground="#ff7f50")
        self.quit_button.pack(side=tk.LEFT, padx=10)

        # Show answer button
        self.answer_button = tk.Button(self.control_frame, text="Show Answer", command=self.show_answer, bg="#ffa500", fg="white", font=("Arial", 14), bd=3, activebackground="#ffcc00")
        self.answer_button.pack(side=tk.LEFT, padx=10)

        # Display attempts count
        self.attempts_label = tk.Label(self.root, text="Attempts: 0", font=("Arial", 12), bg="#f0f8ff", fg="#00008b")
        self.attempts_label.pack(pady=10)

        # Display additional game info
        self.info_label = tk.Label(self.root, text="Game information will appear here.", font=("Arial", 12), bg="#f0f8ff", fg="#00008b")
        self.info_label.pack(pady=10)

    def start_game(self):
        # Get the player's name
        self.player_name = self.name_entry.get().strip()
        if not self.player_name:  # Check if player entered a name
            messagebox.showerror("Notice", "Please enter your name! Remember to click 'Start Game'.")
            return
        
        # Reset the game
        self.secret_number = random.randint(1, 1000)
        self.attempts = 0
        self.current_guesses = []
        self.guess_entry.delete(0, tk.END)
        
        # Reset the hint
        self.hint_label.config(text="Hint will appear here.")
        self.attempts_label.config(text="Attempts: 0")
        
        # Update the game info (do not show secret number yet)
        self.info_label.config(text=f"Player: {self.player_name}\nGuessed Numbers: {self.current_guesses}\nAttempts: {self.attempts}")

        messagebox.showinfo("Notice", f"Welcome {self.player_name} to the game! Start guessing a new number!")

    def save_history(self):
        try:
            # Save game history to the CSV file
            with open(self.history_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.player_name, self.secret_number, self.current_guesses, self.attempts])
            print(f"Successfully saved: {self.player_name}, {self.secret_number}, {self.current_guesses}, {self.attempts}")
        except Exception as e:
            print(f"Error saving history: {e}")

    def show_answer(self):
        """ Show the secret answer when the player clicks 'Show Answer' """
        messagebox.showinfo("Answer", f"The secret number is: {self.secret_number}")

    def check_guess_event(self, event):
        # Handle Enter key event
        self.check_guess()

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            self.current_guesses.append(guess)  # Store the guessed number
            self.attempts_label.config(text=f"Attempts: {self.attempts}")

            # Update game info on the interface
            self.info_label.config(text=f"Player: {self.player_name}\nGuessed Numbers: {self.current_guesses}\nAttempts: {self.attempts}")

            if guess > self.secret_number:
                self.hint_label.config(text="HINT: Too high! Try a smaller number.")
            elif guess < self.secret_number:
                self.hint_label.config(text="HINT: Too low! Try a larger number.")
            else:
                self.hint_label.config(text=f"Congrats! You guessed the lucky number! It's {self.secret_number}!")
                messagebox.showinfo("Victory", f"You guessed the number {self.secret_number} after {self.attempts} attempts!")
                
                # Save history after correct guess
                self.save_history()
                
                # Update game info, display secret number after guessing correctly
                self.info_label.config(text=f"Player: {self.player_name}\nSecret Number: {self.secret_number}\nGuessed Numbers: {self.current_guesses}\nAttempts: {self.attempts}")
                
                self.start_game()  # Start a new game
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()

