points = 0
question1 = "Colour of sun?"
question2 = "Name of the best city to live?"
answer1 = 'yellow'
answer2 = 'Gdańsk'


def quizz_question(question, correct_answer, inter_points):
    print(question)
    answer = input("Your answer is: ")
    if str(answer).lower() == str(correct_answer).lower():
        print('Corretto!')
        inter_points += 1
    else:
        print(f'Wrong answer. Correct was: {correct_answer}')
    return inter_points


print('Welcome in quizz! Do you wanna play a game?')
decision = input('yes/no: ')

if str(decision) == 'yes':
    print('Awesome, lets do this')

    points = quizz_question(question1, answer1, points)
    points = quizz_question(question2, answer2, points)
    points = quizz_question('which programing language is the best?', 'Python', points)

    # print('Colour of sun?')
    # answer1 = input()
    # if str(answer1) == 'yellow':
    #     print('Corretto!')
    #     points += 1
    # else:
    #     print('Wrong answer')
    #
    # print('Name of the best city to live?')
    # answer2 = input()
    # if str(answer2) == 'Gdańsk':
    #     print('Corretto!')
    #     points += 1
    # else:
    #     print('Wrong answer')

    print(f'Great job! You earned {points} points')
else:
    print('to naura')
