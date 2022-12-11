# day9_1.py

from collections import defaultdict
import numpy as np


def get_moves(filename: str) -> tuple:
    with open(filename, mode='r') as f:
        for line in f:
            direction, count = line.strip().split()
            yield direction, int(count)


class Head:
    def __init__(self, position_x=0, position_y=0):
        self.x = position_x
        self.y = position_y

    def process_move(self, direction):
        match direction:
            case "U":
                self.y += 1
            case "D":
                self.y -= 1
            case "R":
                self.x += 1
            case "L":
                self.x -= 1


def is_head_touching(diff_vector):
    if np.linalg.norm(diff_vector) < 2:
        return True
    return False


def count_visited_places(visited_places: dict) -> int:
    return len(visited_places)


class Tail:
    def __init__(self, position_x=0, position_y=0):
        self.visited_places = defaultdict(int)
        self.x = position_x
        self.y = position_y
        self.visited_places[(self.x, self.y)] = 1

    def chase_head(self, head_x, head_y):
        diff_vector = self.calculate_diff_vector(head_x, head_y)
        if is_head_touching(diff_vector):
            pass
        else:
            self.x += int(round(diff_vector[0] / 1.9))
            self.y += int(round(diff_vector[1] / 1.9))
            self.visited_places[(self.x, self.y)] += 1

    def calculate_diff_vector(self, head_x, head_y):
        vector_tail = np.array([self.x, self.y])
        vector_head = np.array([head_x, head_y])
        return vector_head - vector_tail


if __name__ == "__main__":
    moves = get_moves("input.txt")
    start = (0, 0)
    H = Head(start[0], start[1])
    T = Tail(start[0], start[1])
    for move_direction, move_count in moves:
        for _ in range(move_count):
            H.process_move(move_direction)
            T.chase_head(H.x, H.y)
    print(T.visited_places)
    print(count_visited_places(T.visited_places))
