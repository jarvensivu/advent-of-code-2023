from pathlib import Path
from utils import read_input

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

def find_digits_in_letters(line):
  first_digit = last_digit = None
  for key in digit_dictionary.keys():
    first_digit_index = line.find(key)
    last_digit_index = line.rfind(key)

    if first_digit_index != -1:
      if first_digit is None:
        first_digit = (first_digit_index, digit_dictionary[key])
        last_digit = (last_digit_index, digit_dictionary[key])
      else:
        if first_digit_index < first_digit[0]:
          first_digit = (first_digit_index, digit_dictionary[key])
        if last_digit_index > last_digit[0]:
          last_digit = (last_digit_index, digit_dictionary[key])
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

def process_line(line, include_digits_in_letters):
  digits = find_digits(line)

  if include_digits_in_letters:
    digits_in_letters = find_digits_in_letters(line)
    if digits_in_letters[0] is None or digits_in_letters[1] is None:
      return int(digits[0][1] + digits[1][1])
    
    if digits[0] is None or digits_in_letters[0][0] < digits[0][0]:
      digits[0] = digits_in_letters[0]

    if digits[1] is None or digits_in_letters[1][0] > digits[1][0]:
      digits[1] = digits_in_letters[1]

  return int(digits[0][1] + digits[1][1])

def process_file(file_path, include_str_digits):
  file_content = read_input(file_path)
  if file_content:
    return sum(process_line(line, include_str_digits) for line in file_content)
  return 0

def day_01():
    print("Advent of Code - day 1")
    file_path = Path('.', 'data', 'input_01.txt')
    solution1 = process_file(file_path, False)
    print(f"Solution for part one is: {solution1}")
    solution2 = process_file(file_path, True)
    print(f"Solution for part two is: {solution2}")

day_01()
