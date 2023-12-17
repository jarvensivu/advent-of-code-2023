from pathlib import Path
from utils import read_input
from functools import reduce

digit_dictionary = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def update_digits(line, digits):
    first_results = [(line.find(key), value) for key, value in digit_dictionary.items() if key in line] + [digits[0]]
    last_results = [(line.rfind(key), value) for key, value in digit_dictionary.items() if key in line] + [digits[1]]

    first_digit = reduce(lambda x, y: x if x[0] < y[0] else y, first_results)
    last_digit = reduce(lambda x, y: x if x[0] > y[0] else y, last_results)

    return [first_digit, last_digit]


def find_digits(line):
    first_digit = last_digit = None
    for index, char in enumerate(line):
        if char.isdigit():
            if first_digit is None:
                first_digit = last_digit = (index, char)
            else:
                last_digit = (index, char)
    return [first_digit, last_digit]


def part_one(line):
    digits = find_digits(line)
    return int(digits[0][1] + digits[1][1])


def part_two(line):
    digits = find_digits(line)
    digits = update_digits(line, digits)

    return int(digits[0][1] + digits[1][1])


def day_01():
    print("Advent of Code - day 1")
    file_path = Path('.', 'data', 'input_01.txt')
    file_content = read_input(file_path)
    if file_content:
        solution1 = sum(part_one(line) for line in file_content)
        print(f"Solution for part one: {solution1}")
        solution2 = sum(part_two(line) for line in file_content)
        print(f"Solution for part two: {solution2}")


day_01()
