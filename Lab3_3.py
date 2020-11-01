import sys
import pickle


def read_bin_file(file):
    try:
        with open(file, 'rb') as f:
            owners_numbers = pickle.load(f)
    except (FileNotFoundError, pickle.UnpicklingError):
        print('Error: There was a problem with at least one of the files.')
        sys.exit()
    return owners_numbers


def read_txt_files(files):
    try:
        numbers = []
        for file in files:
            with open(file, 'r') as f:
                numbers.append(f.readlines())
    except FileNotFoundError:
        print('Error: There was a problem with at least one of the files.')
        sys.exit()
    return numbers


def display_menu():
    print()
    print('1. Add file')
    print('2. Calculate')
    print()


def cross_reference(files):
    files = read_txt_files(files)
    list_of_sets = []
    for i in range(len(files)):
        nums_stripped = set([n.strip('\n') for n in files[i]])
        list_of_sets.append(nums_stripped)
    nums_in_all = set.intersection(*list_of_sets)
    return nums_in_all


def map_numbers_to_names(numbers, filename):
    owners = read_bin_file(filename)
    unknown = [n for n in numbers if n not in owners.keys()]
    unknown = ['Unknown ' + '(' + n + ')' for n in unknown]
    mapped_names = [v for k, v in owners.items() if k in numbers]
    return mapped_names + unknown


def display_suspects(names):
    msg = 'The following persons was present on all crime scenes:'
    print(msg)
    print(len(msg) * '-')
    if not names:
        print('No matches')
    else:
        for e in names:
            print(e)


def main():
    args = sys.argv[1:]
    if not args:
        print('Check command line arguments')
        sys.exit()
    files = [sys.argv[1]]
    while(True):
        display_menu()
        choice = input('Enter a choice: ')
        if choice == '1':
            file = input('Enter a filename (include full path): ')
            files.append(file)
        if choice == '2':
            numbers = cross_reference(files[1:])
            names = map_numbers_to_names(numbers, files[0])
            display_suspects(names)
            sys.exit()


if __name__ == '__main__':
    main()
