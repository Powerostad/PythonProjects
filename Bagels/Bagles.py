import random

num_digits = 3
max_guesses = 10

def main():
    print(f'''    Hello Welcome to the Bagles
    a diductive logic Game
    
    I am thinking of a {num_digits}-digit number with no repeated digits.
    Try to guess what it is.Here are some clues:
    When i say:     That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.
    
    For example if the secret number was 523 and your guess was 326, the
    clues would be Fermi Pico.''')

    while True:
        secretNum = getSecretNum()
        print('I pick the number i want.')
        print(f'You have {max_guesses} guesses to guess it.')
        guessNum = 1

        while guessNum <= max_guesses:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess {guessNum}:')
                guess = input('> ')
            
            clues = getClues(guess,secretNum)
            print(clues)
            guessNum += 1

            if guess == secretNum:
                break
            if guessNum > max_guesses:
                print('You ran out of guesses.')
                print(f'The secret number was {secretNum}.')

        print('Do you want play again ?(yes or no)')
        if not input('> ').lower().startswith('y'):
            print('Thank you for playing.')
            break




def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''

    for i in range(num_digits):
        secretNum += numbers[i]
    return secretNum


def getClues(guess,secretnum):
    if guess == secretnum:
        return 'You got it!'

    clues = []

    for i in range(num_digits):
        if guess[i] == secretnum[i]:
            clues.append('Fermi')
        elif guess[i] in secretnum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()