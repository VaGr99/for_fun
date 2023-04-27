from random import *

words = ['человек', 'кошка', 'самолет', 'вертолет', 'автомобиль', 'здание', 'фестиваль']


def get_word():
    return choice(words).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def sam_durak(c):
    while not c.isalpha():
        print('Введите букву!: ')
        c = input().upper()
    return c


def is_already_been(c, guessed_letters):
    c = sam_durak(c)
    while c in guessed_letters:
        print('Такая буква уже была! Введите другую: ')
        c = input().upper()
    return c


def play():
    word = get_word()
    word_completion = '_' * len(word)
    guessed_letters = []
    tries = 6
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(f'Я загадал слово из {len(word)} букв: ', *list(word_completion))
    print(f'У Вас есть {tries} попыток, что отгадать слово!')
    while True:
        if word_completion == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            break
        c = is_already_been(input('Введите букву или слово целиком: ').upper(), guessed_letters)
        print(c)
        if c in word:
            for i in range(len(word)):
                if word[i] in c:
                    word_completion = word_completion[:i] + word[i] + word_completion[i + 1:]
                    if word[i] not in guessed_letters:
                        guessed_letters.append(word[i])
            print('Верно!', *list(word_completion))
        else:
            tries -= 1
            print('Такой буквы нет!', display_hangman(tries))
            if tries == 0:
                print('Вы проиграли!', display_hangman(tries))
                print(f'Слово, которое я загадал: {word}')
                break
            else:
                print(f'У Вас осталось {tries} попыток')
    return word


while words:
    y = play()
    words.remove(y.lower())
    x = input('Сыграть ещё раз? да /нет: ')
    if x in 'нет':
        print('Всего хорошего!')
        break
    continue
else:
    print('Вы отгадали все слова!')