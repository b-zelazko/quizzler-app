from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score = 0", fg="white", bg=THEME_COLOR, font=("", 12, "bold italic"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, heigh=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("", 16, "bold italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.get_next_question()
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(self.canvas, bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)

        else:
            self.canvas.itemconfig(self.question_text,
                                   text="You have reached the end of the quiz. Check your score!",
                                   fill=THEME_COLOR
                                   )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        self.canvas.itemconfig(self.question_text, fill="white")
        if is_right:
            self.canvas.config(self.canvas, bg="green")
        else:
            self.canvas.config(self.canvas, bg="red")

        self.window.after(2000, self.get_next_question)
