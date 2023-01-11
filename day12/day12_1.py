# day12_1.py

from string import ascii_lowercase

start_coordinates = None
end_coordinates = None
terrain = []
width = None
length = None
visited = []


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


def find_way(starting_point):
    global end_coordinates, visited
    nodes_to_analyze = [starting_point]
    visited = []
    steps_till_end = 0
    while True:
        new_nodes = []
        print(nodes_to_analyze)
        for node in nodes_to_analyze:
            for candidate in find_next_step(node):
                if candidate not in new_nodes:
                    new_nodes.append(candidate)
            visited.append(node)
        nodes_to_analyze = new_nodes
        steps_till_end += 1
        print(steps_till_end)
        if end_coordinates in visited:
            print(f"Reached the end in {steps_till_end - 1} steps.")
            break
        if steps_till_end > 530:
            break
    return steps_till_end - 1

def find_next_step(spot) -> list:
    global width, length
    x = spot[0]
    y = spot[1]
    possible_directions = []
    if x > 0:
        if can_we_go_there(spot, (x - 1, y)):
            possible_directions.append((x - 1, y))
    if x < length:
        if can_we_go_there(spot, (x + 1, y)):
            possible_directions.append((x + 1, y))
    if y > 0:
        if can_we_go_there(spot, (x, y - 1)):
            possible_directions.append((x, y - 1))
    if y < width:
        if can_we_go_there(spot, (x, y + 1)):
            possible_directions.append((x, y + 1))
    return possible_directions


def can_we_go_there(spot, possible_next_step):
    global visited
    current_spot_height = terrain[spot[0]][spot[1]]
    next_spot_height = terrain[possible_next_step[0]][possible_next_step[1]]
    if (possible_next_step not in visited) and (current_spot_height + 1 >= next_spot_height):
        return True
    return False


if __name__ == "__main__":
    get_terrain("input.txt")
    find_way(start_coordinates)
