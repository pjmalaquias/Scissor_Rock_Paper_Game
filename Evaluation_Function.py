# Possible_inputs = ['Scissor', 'Rock', 'Paper']

def whowin(human, cpu):
    if human == cpu:
        return 0
    elif human == 'Scissor' and cpu == 'Rock':
        return -1
    elif human == 'Scissor' and cpu == 'Paper':
        return +1
    elif human == 'Rock' and cpu == 'Scissor':
        return +1
    elif human == 'Rock' and cpu == 'Paper':
        return -1
    elif human == 'Paper' and cpu == 'Scissor':
        return -1
    elif human == 'Paper' and cpu == 'Rock':
        return +1
    else:
        return 0
