import random
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Rock Paper Scissors")

rock_image = Image.open("./rock.jpeg").resize((100, 100))
paper_image = Image.open("./paper.jpeg").resize((100, 100))
scissor_image = Image.open("./scissor.jpeg").resize((100, 100))


rock_image = ImageTk.PhotoImage(rock_image)
paper_image = ImageTk.PhotoImage(paper_image)
scissor_image = ImageTk.PhotoImage(scissor_image)

game_images = [rock_image, paper_image, scissor_image]

def play_game():
    user_choice = int(user_entry.get())
    user_image.config(image=game_images[user_choice],)

    computer_choice = random.randint(0, 2)
    computer_image.config(image=game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        result_label.config(text="You typed an invalid number, you lose!", fg="orange")
    elif user_choice == computer_choice:
        result_label.config(text="It's a draw", fg="purple")
    elif (user_choice - computer_choice) % 3 == 1:
        result_label.config(text="You win!", fg="green")
    else:
        result_label.config(text="You lose", fg="red")

user_choice_label = tk.Label(root, text="What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.", fg="black")
user_choice_label.pack()

user_entry = ttk.Combobox(root, values=["0", "1", "2"])
user_entry.set("choose")
user_entry.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

user_image = tk.Label(root, image=None)
user_image.pack()

computer_image = tk.Label(root, image=None)
computer_image.pack()

result_label = tk.Label(root, text="", fg="white")
result_label.pack()

root.mainloop()