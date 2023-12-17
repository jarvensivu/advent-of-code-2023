from math import lcm
from pathlib import Path
from utils import read_input


def create_network(file_content):
    network = {}
    for line in file_content:
        network[line[0:3]] = (line[7:10], line[12:15])
    return network


def find_next(current_node, path, network, position):
    options = network[current_node]
    direction = path[position]
    if direction == "L":
        current_node = options[0]
    elif direction == "R":
        current_node = options[1]
    return current_node


def update_position(position, path_length):
    position += 1
    if position >= path_length:
        position = 0
    return position


def part_one(path, network_data):
    network = create_network(network_data)
    steps = 0
    position = 0
    node = "AAA"
    while node != "ZZZ":
        node = find_next(node, path, network, position)
        position = update_position(position, len(path))
        steps += 1
    return steps


def part_two(path, network_data):
    network = create_network(network_data)
    steps = 0
    steps_needed = []
    position = 0
    nodes = [node for node in network if node[2] == "A"]
    current_node = nodes[0]
    while nodes:
        if current_node[2] == "Z":
            steps_needed.append(steps)
            nodes.pop(0)
            steps = 0
            if nodes:
                current_node = nodes[0]
        current_node = find_next(current_node, path, network, position)
        position = update_position(position, len(path))
        steps += 1
    return lcm(*steps_needed)


def day_08():
    print("Advent of Code - day 8")
    file_path = Path('.', 'data', 'input_08.txt')
    file_content = read_input(file_path)
    if file_content:
        solution1 = part_one(file_content[0], file_content[2:])
        print(f"Solution for part one: {solution1}")
        solution2 = part_two(file_content[0], file_content[2:])
        print(f"Solution for part two: {solution2}")


day_08()
