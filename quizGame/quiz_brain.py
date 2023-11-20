
class QuizBrain:
    def __init__(self, qlist):
        self.questionNumber = 0
        self.questionList = qlist
        self.score = 0

    def nextQuestion(self):
        questionNumber = self.questionNumber
        questionList = self.questionList
        currentQuestion = questionList[questionNumber]
        self.questionNumber += 1
        userAnswer = input(f"Q. {self.questionNumber}: {currentQuestion.text}  (True/False)")
        self.check_answer(userAnswer, currentQuestion.answer)
    def still_has_questions(self):
        return self.questionNumber < len(self.questionList)  # returns True or False

    def check_answer(self, userAnswer, currentQuestion):
        if userAnswer.lower() == currentQuestion.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was {currentQuestion}")
        print(f"Your current score is {self.score}/{self.questionNumber} \n")

