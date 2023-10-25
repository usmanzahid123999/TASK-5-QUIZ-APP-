import tkinter as tk
from tkinter import messagebox
import random

# Define a list of quiz questions and answers. Each question is a dictionary.
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "correct_answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "correct_answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Go", "B. Gd", "C. Gl", "D. Au"],
        "correct_answer": "D"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.score = 0
        self.question_index = 0

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 14), command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(pady=10, padx=20, ipadx=10, ipady=5, fill='both')
            
        self.next_question()

    def next_question(self):
        if self.question_index < len(questions):
            self.current_question = questions[self.question_index]
            self.question_label.config(text=self.current_question["question"])
            for i in range(4):
                self.option_buttons[i].config(text=self.current_question["options"][i])
            self.question_index += 1
        else:
            self.show_result()

    def check_answer(self, selected_index):
        selected_option = self.current_question["options"][selected_index]
        if selected_option.startswith(self.current_question["correct_answer"]):
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Your answer is incorrect. The correct answer is {self.current_question['correct_answer']}.")

        self.next_question()

    def show_result(self):
        result_message = f"You got {self.score} out of {len(questions)} questions correct."
        messagebox.showinfo("Quiz Results", result_message)
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.score = 0
            self.question_index = 0
            self.next_question()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.geometry("600x400")  # Set the initial window size
    root.mainloop()
