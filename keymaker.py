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
    print(solution)


shift_characters("zozo", 5)


def pad_up_to(word, shift, n):
    word=word.lower()
    solution=""
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
    print(solution)

pad_up_to("asd", 2, 11)


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
    print(solution)

abc_mirror("asd")


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    pass


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    pass


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    pass


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    pass


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
