import prompt


def game(rule, function):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rule())
    i = 0
    while i < 3:
        question, right_answer = function()
        print(f'Question: {question}')
        answer = prompt.string()
        print(f'Your answer: {answer}')
        if answer == right_answer:
            print('Correct!')
            i += 1
        else:
            print(
                f"{answer} is wrong answer ;(. "
                f"Correct answer was {right_answer}."
            )
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')
