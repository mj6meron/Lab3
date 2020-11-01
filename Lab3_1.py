import sys
import pickle


def read_file(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    return data


def map_to_int(measurements):
    data_int = {k: int(v.strip('°')) for k, v in measurements.items()}
    return data_int


def find_faulty(primary, secondary, threshold):
    p = primary
    s = secondary
    t = threshold
    gt_threshold = {key for key in p.keys() if abs(p.get(key)-s.get(key)) > t}
    return gt_threshold


def display_warnings(faulty_sensors):
    msg = 'Analyzis of the provided files is complete.'
    print()
    print(msg)
    print(len(msg) * '-')
    print()
    print('The following sensors differ more than 2°:')
    for e in faulty_sensors:
        print(e)


def main():
    args = sys.argv[1:]
    if not args or len(args) < 2:
        print('Check command line arguments')
        sys.exit()
    try:
        data1 = read_file(sys.argv[1])
        data2 = read_file(sys.argv[2])
    except (FileNotFoundError, pickle.UnpicklingError):
        print('Error: The files given as arguments are not valid.')
    else:
        data_int1 = map_to_int(data1)
        data_int2 = map_to_int(data2)
        faulty_sensors = find_faulty(data_int1, data_int2, 2)
        display_warnings(faulty_sensors)


if __name__ == "__main__":
    main()
