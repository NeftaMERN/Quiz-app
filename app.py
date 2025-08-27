
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

if __name__ == "__main__":
    run_questions(questions)