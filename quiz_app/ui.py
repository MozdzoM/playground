from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window  = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #Labels
        self.score_label = Label(text=f"Score: <NUMBER>", bg=THEME_COLOR, )
        self.score_label.grid(row=0, column=1)

        #Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness="0")
        self.quiz_question = self.canvas.create_text(
            150, 125,
            width=280,
            text="<QUESTION>",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #Button Images
        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        #Buttons
        self.true_button = Button(image=true_image, bd="0", command=self.guess_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_image, bd="0", command=self.guess_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_question, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_question,
                text="There are no more questions. Restart the app."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def guess_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def guess_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
