# day7_2.py
import re

from day7_1 import get_directories


def find_smallest_dir_above_size(filename: str) -> int:
    dir_sizes = get_directories(filename)
    space_to_free_up = calculate_space_to_free_up(dir_sizes)
    result = min(size for size in dir_sizes.values() if size >= space_to_free_up)
    return result


def calculate_space_to_free_up(dir_sizes: dict) -> int:
    free_space = 70_000_000 - dir_sizes["//"]
    space_to_free_up = 30_000_000 - free_space
    return space_to_free_up


def first_small_dirs():
    print(find_smallest_dir_above_size("input.txt"))


if __name__ == "__main__":
    first_small_dirs()
