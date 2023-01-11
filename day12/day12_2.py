# day12_2.py

from day12_1 import get_terrain, terrain, find_way

def find_best_trail():
    trail_length = []
    for row_no, row in enumerate(terrain):
        for position_no, elevation in enumerate(row):
            if elevation == 0:
                print(f"{row_no}, {position_no}")
                start_coordinates = (row_no, position_no)
                trail_length.append(find_way(start_coordinates))
    print(trail_length)
    print(f"best trail is {min(trail_length)}")



if __name__ == "__main__":
    get_terrain("input.txt")
    find_best_trail()
