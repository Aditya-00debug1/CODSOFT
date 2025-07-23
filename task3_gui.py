import tkinter as tk
import random


root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("420x400")
root.configure(bg="#e6f2ff")
root.resizable(False, False)


user_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]


def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!", fg="orange")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You Win!", fg="green")
        user_score += 1
    else:
        result_label.config(text="Computer Wins!", fg="red")
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")


title = tk.Label(root, text="Rock - Paper - Scissors", font=("Helvetica", 20, "bold"), bg="#e6f2ff", fg="#333")
title.pack(pady=15)

instruction = tk.Label(root, text="Choose your move:", font=("Helvetica", 14), bg="#e6f2ff")
instruction.pack()


button_frame = tk.Frame(root, bg="#e6f2ff")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, height=2, font=("Helvetica", 12),
                        command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, height=2, font=("Helvetica", 12),
                         command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, height=2, font=("Helvetica", 12),
                            command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

computer_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#e6f2ff")
computer_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#e6f2ff")
result_label.pack(pady=5)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 14), bg="#e6f2ff")
score_label.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), bg="red", fg="white", width=10, command=root.destroy)
exit_button.pack(pady=10)


root.mainloop()
