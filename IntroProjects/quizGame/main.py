from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    newQuestion = Question(text, answer)
    question_bank.append(newQuestion)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nextQuestion()

print(f"You've completed the quiz. Your final score was {quiz.score}/ {quiz.questionNumber}")