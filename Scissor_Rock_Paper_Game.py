# programming the scissor - rock - papper game

# game will ask for a input
# computer will randomly choose also a input
# user vs. computer
# add to score
# from random import randint
# from Evaluation_Function import whowin
# Possible_inputs = ['Scissor', 'Rock', 'Paper']


def Play():
    from random import randint
    from Evaluation_Function import whowin
    Score_U = 0
    Score_CPU = 0
    Possible_inputs = ['Scissor', 'Rock', 'Paper']

    print('Welcome to the SRP championship!')
    print('The atual score is you: %d vs. computer: %d' % (Score_U, Score_CPU))

    while (True):
        computer_input = Possible_inputs[randint(0, 2)]
        player_input = input('Scissor, Rock or Paper?..')
        if (-(player_input in Possible_inputs)):
            pass

        who_win = whowin(player_input, computer_input)
        if who_win == 0:
            print("User: %s \nComp: %s" % (player_input, computer_input))
            print('Draw...')
            print('SCORE you: %s vs computer: %s\n' % (Score_U, Score_CPU))
        elif who_win == 1:
            Score_U += 1
            print("User: %s \nComp: %s" % (player_input, computer_input))
            print('User Point...')
            print('SCORE you: %s vs computer: %s\n' % (Score_U, Score_CPU))
            if Score_U == 3:
                print('User wins!')
                break
            elif Score_CPU == 3:
                print('Computer wins!')
                break
            else:
                continue
        elif who_win == -1:
            Score_CPU += 1
            print("User: %s \nComp: %s" % (player_input, computer_input))
            print('CPU Point')
            print('SCORE you: %s vs computer: %s\n' % (Score_U, Score_CPU))
            if Score_U == 3:
                print('User wins!')
                break
            elif Score_CPU == 3:
                print('Computer wins!')
                break
            else:
                continue
