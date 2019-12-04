import typing


def good_length(pwd: str, length: int) -> bool:
    return len(pwd) == length


def good_range(pwd: str, lower: int, upper: int) -> bool:
    pwd = int(pwd)
    return (pwd >= lower) and (pwd <= upper)


def adjacency(pwd: str) -> bool:
    for pair in zip(pwd, pwd[1:]):
        if pair[0] == pair[1]:
            return True
    return False


def increasing(pwd: str) -> bool:
    last_digit = pwd[0]
    for digit in pwd[1:]:
        if digit < last_digit:
            return False
        last_digit = digit
    return True


def solve_part1() -> int:
    good_passwords = 0
    for password in range(372037, 905157 + 1):
        password = str(password)
        if adjacency(password) and increasing(password):
            good_passwords += 1
    return good_passwords


def adjacency2(pwd: str) -> bool:
    numbers = {}
    last_digit = pwd[0]
    counter = 1
    for digit in pwd[1:]:
        if digit == last_digit:
            counter += 1
        else:
            numbers.update(
                {str(last_digit): counter}
            )
            counter = 1
        last_digit = digit

    numbers.update(
        {str(digit): counter}
    )

    return 2 in numbers.values()


def solve_part2() -> int:
    good_passwords = 0
    for password in range(372037, 905157 + 1):
        password = str(password)
        if adjacency2(password) and increasing(password):
            good_passwords += 1
    return good_passwords


if __name__ == '__main__':
    # Part 1
    print('Part 1, ', solve_part1())
    # Part 2
    print('Part 2, ', solve_part2())
