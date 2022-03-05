from random import choices, shuffle
from sys import exit

with open('Words.txt', 'r') as f:
    words = f.readlines()
    words = [word.strip() for word in words]


def get_difficulty():
    difficulty = '1' # input('Choose difficulty. Enter 1 for easy or 2 for hard\n')
    if difficulty == '1':
        words_to_guess = choices(words, k=4)*2
        shuffle(words_to_guess)
        chances = 10
        print(f'You have chosen easy. You have {chances} chances to guess {len(words_to_guess)//2} pairs of words \n')
    elif difficulty == '2':
        words_to_guess = choices(words, k=8) * 2
        shuffle(words_to_guess)
        chances = 15
        print(f'You have chosen easy. You have {chances} chances to guess {len(words_to_guess)//2} pairs of words \n')
    return words_to_guess, chances

def get_player_move():
    move = input('Enter coordinates, eg. b2: ')
    print()
    if len(move) > 2:
        print('Bad input! Too long')
        return False
    elif len(move) < 2:
        print('Bad input! Too short!')
        return False

    coord_letter, coord_num = move[0], move[1]

    if  not coord_letter.isalpha():
        print('Bad input! First coordinate should be a letter')
        return False
    if not coord_num.isnumeric() and coord_num not in coords:
        print('Bad input! Second coordinate should be a number')
        return False
    if coord_letter == 'a' or coord_letter == 'b':
        return coord_letter, int(coord_num)
    else:
        print('Bad input! First coordinate out of range')
        return False


def uncover_word(player_move):
    coord_letter, coord_num = player_move
    if coord_letter == 'a':
        a_row_of_x[coord_num] = a_row_of_words[coord_num]
        guessed_word = a_row_of_words[coord_num]
        return a_row_of_x, guessed_word
    elif coord_letter == 'b':
        b_row_of_x[coord_num] = b_row_of_words[coord_num]
        guessed_word = b_row_of_words[coord_num]
        return b_row_of_x, guessed_word

def draw_table(table):
    """Adjusts the amount of spaces, so the table fits the longest uncovered word"""
    max_space = 0
    for list in table:
        for word in list:
            if len(word) > max_space:
                max_space = len(word)

    for list in table:
        line = ' '.join(str(elem).ljust(max_space) for elem in list)
        print(line)
    print()


words_to_guess, chances = get_difficulty()
coords = [' '] + [str(x) for x in range(1, len(words_to_guess)//2+1)]
a_row_of_words = ['A'] + [word for word in words_to_guess[:int(len(words_to_guess)/2)]]
b_row_of_words = ['B'] + [word for word in words_to_guess[int(len(words_to_guess)/2):]]
a_row_of_x = ['A'] + ['X' for word in words_to_guess[:len(words_to_guess)//2]]
b_row_of_x = ['B'] + ['X' for word in words_to_guess[len(words_to_guess)//2:]]

table = [coords] + [a_row_of_x] + [b_row_of_x]
draw_table(table)

while chances >0:
    player_move = get_player_move() # zwraca krotke (coord_letter, int(coord_num)) albo false
    if player_move != False:
        guessed_word_1 = uncover_word(player_move)[-1] # zwraca _row_of_x z odkrytym slowem i zgadniete slowo
    draw_table(table)
    player_move = get_player_move()  # zwraca krotke (coord_letter, int(coord_num)) albo false
    if player_move != False:
        guessed_word_2 = uncover_word(player_move)[-1]  # zwraca _row_of_x z odkrytym slowem i zgadniete slowo
    draw_table(table)

    if guessed_word_1 != guessed_word_2:
        chances -= 1
        print(f"Words don't match! You have failed. Chances left: {chances} \n")
        if chances == 0:
            print('No more chances left, you loose.')
            exit()
        a_row_of_x = ['A'] + ['X' for word in words_to_guess[:len(words_to_guess) // 2]]
        b_row_of_x = ['B'] + ['X' for word in words_to_guess[len(words_to_guess) // 2:]]
        table = [coords] + [a_row_of_x] + [b_row_of_x]
        draw_table(table)

    if a_row_of_x == a_row_of_words and b_row_of_x == b_row_of_words:
        print("You won!")
        exit()

