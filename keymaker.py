

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def shift_characters(word, shift):
    word=word.lower()
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


print(shift_characters("zozo", 5))


def pad_up_to(word, shift, n):
    word=word.lower()
    solution=word
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
        solution+=saver
        word=saver
        saver=""
    return solution[0:n]

print(pad_up_to("abb", 5, 11))


def abc_mirror(word):
    word=word.lower()
    solution=""
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
    solution+=saver
    word=saver
    saver=""
    return solution

print(abc_mirror("asd"))



def create_matrix(word1, word2):
    new_word = ""
    matrix = []
    index = None
    for i in word2:
        index=letters.index(i)
        new_word=shift_characters(word1,index)
        matrix.append(new_word)
    return matrix

print(create_matrix("mamas", "papas"))

def zig_zag_concatenate(matrix):
    word1 = matrix[0]
    word2 = matrix[1]
    word3 = matrix[2]
    word4 = matrix[3]
    solution = word1[0] + word2[0] + word3[0] + word4[0] + word4[1] + word3[1] + word2[1] + word1[1] + word1[2] + word2[2] + word3[2] + word4[2]
    return solution

print(zig_zag_concatenate(["aaa", "bbb", "ccc", "ddd"]))


def rotate_right(word, n):
    word=word.lower()
    letter = [char for char in word]
    letters = [char for char in word]
    for i in range(len(letter)):
        position = 0
        for j in letters:
            if letter[i] == j:
                try:
                    letter[i] = letters[position-n]
                except IndexError:
                    letter[i] = letters[position-(n%4)]
                break
            else:
                position += 1
    solution = "".join(letter)
    return solution

print(rotate_right("abcd", 2))

def get_square_index_chars(word):
    solution=""
    word=word.lower()
    letter = [char for char in word]
    for i in range(len(letter)):
        try:
            solution += letter[i*i]
        except:
            continue
    return solution

print(get_square_index_chars("abcdefghijklm"))


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    pass


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
