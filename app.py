
import random

questions = {
    "What is the capital of France?": "Paris",
    "Who developed Python Programming Language?": "Guido van Rossum",
    "What is 5 + 7?": "12",
    "Which planet is known as the Red Planet?": "Mars",
    "What does HTML stand for?": "HyperText Markup Language"
}

def run_questions(quiz_question):
    score = 0
    print('Welcome')

    for question, answer in quiz_question.items():
        print(question)

        user_answer = input('Enter the answer: ')

        if answer == user_answer:
            print('correct')
            score += 1

        else:
            print(f'not correct the answer is {answer}')

    print(f'score {score}/ {len(quiz_question)}')

# if __name__ == "__main__":
#     run_questions(questions)

def randem_question():

    num1 = random.randint(1,20)
    num2 = random.randint(1,20)

    opreters = random.choice(['+', '-', '*', '/'])

    if opreters == '/':
        num2 = random.randint(1,20)
        answer = round(num1 / num2, 2)
    elif opreters == '+':
        answer = num1 + num2
    elif opreters == '-':
        answer = num1 - num2
    elif opreters == '*':
        answer = num1 * num2

    return f'{num1} {opreters} {num2}', answer

def math():
    score = 0
    for i in range(5):
        question, answer = randem_question()
        print(question)
        user_answer = float(input('Enter answer: '))
        if user_answer == answer:
            print('correct\n')
            score += 1
        else:
            print(f'not correct {answer}')
    print(f'get score {score}/5')

def manu():

    while True:
        print("\n 1.General Programming question")
        print(" 2.Maths question")
        print(" 3.Exit")
        choice = input('Choice one: ')
        