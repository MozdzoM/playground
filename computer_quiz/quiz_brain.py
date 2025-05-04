class QuizBrain:
    """Initializes quiz_brain object."""
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    """Checks if question_list is empty or not."""
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    """Increments question_number and asks next question."""
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: "
                            f"{current_question.text} "
                            f"(True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
