# day12_1.py

from string import ascii_lowercase

start_coordinates = None
end_coordinates = None
terrain = []
width = None
length = None
path_found = False
steps_till_end = []

def get_terrain(filename: str):
    global terrain
    with open(filename, mode='r') as f:
        for row_number, line in enumerate(f):
            row = []
            for position, letter in enumerate(line.strip()):
                if letter == "S":
                    global start_coordinates
                    start_coordinates = (row_number, position)
                    letter = "a"
                if letter == "E":
                    global end_coordinates
                    end_coordinates = (row_number, position)
                    letter = "z"
                row.append(ascii_lowercase.index(letter))
            terrain.append(row)
    global width, length
    width = len(row) - 1
    length = len(terrain) - 1


def find_way(path_so_far: list):
    global steps_till_end
    print(len(path_so_far))
    if len(path_so_far) == 0:
        path_so_far.append(start_coordinates)
    possible_directions = find_next_step(path_so_far)
    if len(possible_directions) == 0:
        print("Dead end")
    for next_step in possible_directions:
        if next_step == end_coordinates:
            print(f"We have reached the end in {len(path_so_far)} steps!")
            print(path_so_far)
            steps_till_end.append(len(path_so_far))
            return
        else:
            copy_path = path_so_far.copy()
            copy_path.append(next_step)
            find_way(copy_path)


def find_next_step(path) -> list:
    global width, length
    last_location = path[-1]
    x = last_location[0]
    y = last_location[1]
    possible_directions = []
    if x > 0:
        if can_we_go_there(path, (x - 1, y)):
            possible_directions.append((x - 1, y))
    if x < length:
        if can_we_go_there(path, (x + 1, y)):
            possible_directions.append((x + 1, y))
    if y > 0:
        if can_we_go_there(path, (x, y - 1)):
            possible_directions.append((x, y - 1))
    if y < width:
        if can_we_go_there(path, (x, y + 1)):
            possible_directions.append((x, y + 1))
    return possible_directions


def can_we_go_there(path, place):
    current_spot_height = terrain[path[-1][0]][path[-1][1]]
    next_spot_height = terrain[place[0]][place[1]]
    if (place not in path) and (current_spot_height + 1 >= next_spot_height):
        return True
    return False


if __name__ == "__main__":
    get_terrain("sample.txt")
    find_way([])
    print(steps_till_end)
    print(min(steps_till_end))
