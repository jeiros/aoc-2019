def read_file(fname):
    with open(fname, 'r') as f:
        data = [int(line.strip()) for line in f]
    return data


def fuel_module(mass):
    return mass//3 - 2


def fuel_recursive(mass, total=0):
    mass = fuel_module(mass)
    if mass > 0:
        total += mass
        return fuel_recursive(mass, total)
    else:
        return total


if __name__ == '__main__':
    data = read_file('input.dat')
    # Tests
    assert fuel_module(12) == 2
    assert fuel_module(14) == 2
    assert fuel_module(1969) == 654
    assert fuel_module(100756) == 33583
    # Part 1
    print("Part 1: ", sum(map(fuel_module, data)))
    # Part 2
    assert fuel_recursive(14) == 2
    assert fuel_recursive(1969) == 966
    assert fuel_recursive(100756) == 50346
    print("Part 2: ", sum(map(fuel_recursive, data)))
