# day8_1.py


def get_forest(filename: str) -> list:
    trees = []
    with open(filename, mode='r') as f:
        for line in f:
            trees.append([int(tree) for tree in line.strip()])
    return trees


def get_trees_visibility(forest: list) -> dict:
    visibility_map = {}
    forest_width = len(forest[0])
    forest_length = len(forest)
    for row_no, row in enumerate(forest):
        for position, tree_height in enumerate(row):
            if is_tree_on_the_edge(row_no, position, forest_length, forest_width):
                visibility_map[(row_no, position)] = 1
                continue
            else:
                if is_tree_visible_from_left_or_right(row, position):
                    visibility_map[(row_no, position)] = 1
                    continue
                if is_tree_visible_from_up_or_down(forest, row_no, position, tree_height):
                    visibility_map[(row_no, position)] = 1
                    continue
            visibility_map[(row_no, position)] = 0
    return visibility_map


def is_tree_on_the_edge(row_no, position, length, width) -> bool:
    if 0 == position or 0 == row_no or width - 1 == position or length - 1 == row_no:
        return True
    return False


def is_tree_visible_from_left_or_right(row, position) -> bool:
    if max(row[:position]) < row[position] or max(row[position + 1:]) < row[position]:
        return True
    return False


def is_tree_visible_from_up_or_down(forest, tree_row_no, tree_position, tree_height) -> bool:
    trees_above = []
    trees_beyond = []
    for row_no, row in enumerate(forest):
        if row_no < tree_row_no:
            trees_above.append(row[tree_position])
        elif row_no > tree_row_no:
            trees_beyond.append(row[tree_position])

    if max(trees_above) < tree_height or max(trees_beyond) < tree_height:
        return True
    return False


def count_visible_trees(visibility_map: dict) -> int:
    print(list(visibility_map.values()).count(1))


if __name__ == "__main__":
    my_forest = get_forest("input.txt")
    vmap = get_trees_visibility(my_forest)
    count_visible_trees(vmap)
