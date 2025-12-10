def título(text):
    print('\33[36m=\33[m' * 50)
    print(f'\033[1;34m{text.upper().center(50)}\033[m')
    print('\33[36m=\33[m' * 50)

def linha(simb):
    print(simb*50)