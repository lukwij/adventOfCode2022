# day9_2.py

import day9_1

if __name__ == "__main__":
    moves = day9_1.get_moves("input.txt")
    start = (0, 0)
    H = day9_1.Head(start[0], start[1])
    tail_list = [day9_1.Tail(start[0], start[1]) for _ in range(9)]
    for move_direction, move_count in moves:
        predecessor = {}
        for _ in range(move_count):
            H.process_move(move_direction)
            predecessor["x"] = H.x
            predecessor["y"] = H.y
            for tail in tail_list:
                tail.chase_head(predecessor["x"], predecessor["y"])
                predecessor["x"] = tail.x
                predecessor["y"] = tail.y
    print(tail_list[-1].visited_places)
    print(day9_1.count_visited_places(tail_list[-1].visited_places))
