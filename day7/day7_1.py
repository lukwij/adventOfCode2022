# day7_1.py
import re


def get_datastream(filename: str) -> str:
    with open(filename, mode='r') as f:
        for line in f:
            yield line


def get_directories(filename: str) -> dict:
    dir_sizes = {}
    path = ""
    current_dir = ""
    for line in get_datastream(filename):
        if line.startswith("$ cd .."):
            path = path[:-(len(current_dir) + 1)]
            current_dir = path.split("/")[-2]
        elif line.startswith("$ cd"):
            current_dir = line.strip().split(" ")[2]
            path = path + current_dir + "/"
            dir_sizes[path] = 0
        elif result := re.match(r"(^\d+)", line):
            for directory in dir_sizes:
                if path.startswith(directory):
                    dir_sizes[directory] += int(result[1])
    return dir_sizes


def find_dirs_below_size(filename: str, max_size: int) -> int:
    dir_sizes = get_directories(filename)
    for directory, size in dir_sizes.items():
        print(f"{directory}: {size}")
    result = sum(dir_sizes[directory] for directory in dir_sizes if dir_sizes[directory] < max_size)
    return result


def first_small_dirs():
    print(find_dirs_below_size("input.txt", 100_000))


if __name__ == "__main__":
    first_small_dirs()
