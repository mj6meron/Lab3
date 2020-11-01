import sys
import pickle
TRANSLATION = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def read_orders(filename):
    with open(filename, 'rb') as f:
        numbers = pickle.load(f)
    return numbers


def read_words(filename):
    with open(filename, 'r') as f:
        words = [word.strip('\n') for word in f.readlines()]
    return words


def find_all_possible_combinations(order_number):
    first_sequence = list(TRANSLATION.get(order_number[0]))
    combinations = first_sequence
    for i in range(1, len(order_number)):
        digit = order_number[i]
        combinations += add_digit(digit, combinations)
    combinations = [c for c in combinations if len(c) == len(order_number)]
    return combinations


def add_digit(digit, combinations):
    sequence = [letter for letter in TRANSLATION.get(digit)]
    comb_part = [a + b for a in combinations for b in sequence]
    return comb_part


def filter_valid_words(possible_combinations, valid_words):
    possible_words = [w for w in possible_combinations if w in valid_words]
    return possible_words


def display_possible_words(order_number, words):
    print(order_number, ': ', end='')
    if words:
        print(words[0])
        for i in range(1, len(words)):
            line = words[i].rjust(13)
            print(line)
    else:
        print(order_number, ': ', 'None')
    print()
    return


def main():
    args = sys.argv[1:]
    if not args or len(args) < 2:
        print('Check command line arguments')
        sys.exit()
    try:
        orders = read_orders(sys.argv[1])
        words = read_words(sys.argv[2])
    except (FileNotFoundError, pickle.UnpicklingError):
        print('Error: There was a problem with at least one of the files.')
    else:
        for order in orders:
            words = [w for w in words if len(w) == len(order)]
            combinations = find_all_possible_combinations(order)
            filtered_words = filter_valid_words(combinations, words)
            display_possible_words(order, filtered_words)


if __name__ == '__main__':
    main()
