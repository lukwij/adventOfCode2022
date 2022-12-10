# day8_2.py

from day8_1 import get_forest


def get_trees_scenic_score(forest: list) -> dict:
    scenic_map = {}
    forest_width = len(forest[0])
    forest_length = len(forest)
    for row_no, row in enumerate(forest):
        for position, tree_height in enumerate(row):
            if is_tree_on_the_edge(row_no, position, forest_length, forest_width):
                scenic_map[(row_no, position)] = 0
                continue
            else:
                row_scenic_score = calculate_row_scenic_score(row, position)
                column_scenic_score = calculate_column_scenic_score(forest, row_no, position, tree_height)
                scenic_map[(row_no, position)] = row_scenic_score * column_scenic_score
    return scenic_map


def is_tree_on_the_edge(row_no, position, length, width) -> bool:
    if 0 == position or 0 == row_no or width - 1 == position or length - 1 == row_no:
        return True
    return False


def calculate_row_scenic_score(row, position) -> int:
    left_scenic_score = 0
    right_scenic_score = 0
    for tree_height in row[:position][::-1]:
        if tree_height < row[position]:
            left_scenic_score += 1
        else:
            left_scenic_score += 1
            break
    for tree_height in row[position + 1:]:
        if tree_height < row[position]:
            right_scenic_score += 1
        else:
            right_scenic_score += 1
            break
    return left_scenic_score * right_scenic_score


def calculate_column_scenic_score(forest, tree_row_no, tree_position, my_tree_height) -> int:
    trees_above = []
    trees_beyond = []
    up_scenic_score = 0
    down_scenic_score = 0
    for row_no, row in enumerate(forest):
        if row_no < tree_row_no:
            trees_above.append(row[tree_position])
        elif row_no > tree_row_no:
            trees_beyond.append(row[tree_position])

    for tree_height in trees_above[::-1]:
        if tree_height < my_tree_height:
            up_scenic_score += 1
        else:
            up_scenic_score += 1
            break
    for tree_height in trees_beyond:
        if tree_height < my_tree_height:
            down_scenic_score += 1
        else:
            down_scenic_score += 1
            break
    return up_scenic_score * down_scenic_score


def find_highest_score(scenic_map: dict):
    print(max(scenic_map.values()))


if __name__ == "__main__":
    my_forest = get_forest("input.txt")
    smap = get_trees_scenic_score(my_forest)
    find_highest_score(smap)
