import string

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                                                                                                "w", "x", "y", "z"]


def shift_characters(word, shift):
    word = word.lower()
    letter = [char for char in word]
    for i in range(len(letter)):
        position = 0
        for j in letters:
            if letter[i] == j:
                try:
                    letter[i] = letters[position+shift]
                except IndexError:
                    letter[i] = letters[shift-(26-position)]
                break
            else:
                position += 1
    solution = "".join(letter)
    return solution


def pad_up_to(word, shift, n):
    solution = word
    while len(solution) <= n:
        letter = [char for char in word]
        for i in range(len(letter)):
            position = 0
            for j in letters:
                if letter[i] == j:
                    try:
                        letter[i] = letters[position+shift]
                    except IndexError:
                        letter[i] = letters[shift-(26-position)]
                    break
                else:
                    position += 1
        saver = "".join(letter)
        solution += saver
        word = saver
        saver = ""
    return solution[0:n]


def abc_mirror(word):
    word = word.lower()
    solution = ""
    letter = [char for char in word]
    for i in range(len(letter)):
        position = 0
        for j in letters:
            if letter[i] == j:
                try:
                    letter[i] = letters[-position-1]
                except IndexError:
                    letter[i] = letters[position+1]
                break
            else:
                position += 1
    saver = "".join(letter)
    solution += saver
    word = saver
    saver = ""
    return solution


def create_matrix(word1, word2):
    new_word = ""
    matrix = []
    index = None
    letters = string.ascii_lowercase
    for i in word2:
        index = letters.index(i)
        new_word = shift_characters(word1, index)
        matrix.append(new_word)
    return matrix


def zig_zag_concatenate(matrix):
    solution = ""
    solution1 = ""
    solution3 = ""
    turn = 0
    while turn != len(matrix):
        for i in range(len(matrix)):
            if turn % 2 == 0:
                for j in matrix:
                    solution += j[turn]
                solution3 += solution
                solution = ""
            else:
                for j in matrix:
                    solution1 += j[turn]
                solution2 = solution1[::-1]
                solution3 += solution2
                solution1 = ""
            turn += 1
    return solution3


def rotate_right(word, n):
    letter = [char for char in word]
    letters = [char for char in word]
    letters2 = [char for char in word]
    for i in range(len(letter)):
        position = 0
        for j in letters2:
            if letter[i] == j:
                try:
                    letter[i] = letters[position-n]
                except IndexError:
                    un = n//len(letter)
                    n = n - un*len(letter)
                    letter[i] = letters[position-n]
                letters2[position] = "."
                break
            else:
                position += 1
    solution = "".join(letter)
    return solution


def get_square_index_chars(word):
    solution = ""
    word = word.lower()
    letter = [char for char in word]
    for i in range(len(letter)):
        try:
            solution += letter[i*i]
        except():
            continue
    return solution


def remove_odd_blocks(word, block_length):
    word = word.lower()
    letter = [char for char in word]
    three = []
    block = ""
    turn = 0
    solution = []
    solution2 = ""
    for i in range(len(letter)):
        three += letter[i]
        block = "".join(three)
        turn += 1
        if turn == block_length:
            solution.append(block)
            turn = 0
            three = []
            block = ""
    solution.append(block)
    try:
        for i in range(len(solution)):
            if i % 2 == 1:
                del solution[i]
    except():
        i = i
    for j in range(len(solution)):
        solution2 += solution[j]
    return solution2


def reduce_to_fixed(word, n):
    word2 = pad_up_to(word, 0, 6)
    n = n//3
    word3 = rotate_right(word2, -n)
    return word3[::-1]


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    print(padded)
    print(abc_mirror(padded))
    print(create_matrix(padded, abc_mirror(padded)))
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    print(elongated)
    rotated = rotate_right(elongated, 3000003)
    print(rotated)
    cherry_picked = get_square_index_chars(rotated)
    print(cherry_picked)
    halved = remove_odd_blocks(cherry_picked, 3)
    print(halved)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
