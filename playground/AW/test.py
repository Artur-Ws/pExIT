points = 0
question1 = "Year of Grunwald's battle?"
question2 = "Exact time of the polish pope death? put in format HH:MM"
answer1 = '1410'
answer2 = '21:37'


def quizz_question(question, correct_answer, inter_points):
    print(question)
    answer = input('Your answer is: ')
    if str(answer).lower().lstrip() == str(correct_answer).lower().lstrip():
        print('Correct!')
        inter_points += 1
    else:
        print(f'Wrong answer. Correct was: {correct_answer}')
    return inter_points


print('Welcome in quizz app! Do you want to play?')
decision = input('yes/no: ')

if str(decision) == 'yes':
    print('Great, lets go')

    points = quizz_question(question1, answer1, points)
    points = quizz_question(question2, answer2, points)
    points = quizz_question(correct_answer='Python', question='which programing language is the best?',
                            inter_points=points)

    #
    # print("Year of Grunwald's battle?")
    # answer1 = input()
    # correct1 = '1410'
    # if str(answer1) == correct1:
    #     print('Correct!')
    #     points += 1
    # else:
    #     print(f'Wrong answer. Correct was: {correct1}')
    #
    # print("Exact time of the polish pope death? put in format HH:MM")
    # answer2 = input()
    # correct2 = '21:37'
    # if str(answer2) == correct2:
    #     print('Correct!')
    #     points += 1
    # else:
    #     print(f'Wrong answer. Correct was: {correct2}')

    print(f'Great job! You earned {points} points')
else:
    print('to spierdalaj')







# if False:
#     print('its true')
#
# else:
#     print('its false')

# if 5:
#     print('its true')



# print(decision)





# integer = 5
# float1 = 5.67
# string1 = str('abc')
#
# print(float1)
# x = 'Jestem Artur mam '
# y = int(26)
# print(f"Jestem Artur, mam {y} lat")
#
# tuple = (1, 2, 3, 4)
# list = [1, 'jabłko', True, 4]
#
# print(tuple)
#
# list[2] = 'banan'
#
# print(list)
#
#
