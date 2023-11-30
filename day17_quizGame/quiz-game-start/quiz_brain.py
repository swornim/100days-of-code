#TODO: asking the questions
#TODO: checking if the answer is correct or not
#TODO: checking if we're the end of the quiz

class QuizBrain:
    def __init__(self,q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1} : {self.question_list[self.question_number].text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self,user_answer,correct_answer): 
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
        else:
            print("that's wrong.")

        print(f"the correct answer was: {correct_answer}")

        print(f"Your current score is : {self.score}/{self.question_number}")