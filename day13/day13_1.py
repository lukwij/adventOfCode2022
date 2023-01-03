# day13_1.py

def get_pairs(filename: str) -> list:
    pairs = []
    pair = []
    with open(filename, mode='r') as f:
        for line in f:
            line_stripped = line.strip()
            if line_stripped:
                entry = eval(line_stripped)
                pair.append(entry)
            if 2 == len(pair):
                pairs.append(pair)
                pair = []
    return pairs


def compare_pairs(pairs: list) -> list:
    results = []
    for pair in pairs:
        results.append(compare_item(pair[0], pair[1]))
    return results


def sum_up_indices(comparison_results: list) -> int:
    summed_up_indices = 0
    for i, result in enumerate(comparison_results):
        if result == "yes":
            summed_up_indices += (i + 1)
    return summed_up_indices


def compare_item(left, right):
    if not left and right:
        return "yes"
    if left and not right:
        return "no"
    for i, item in enumerate(left):
        if (len(right) - 1) < i:
            return "no"
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return "yes"
            elif left[i] > right[i]:
                return "no"
        else:
            if isinstance(left[i], list) and isinstance(right[i], list):
                if result := compare_item(left[i], right[i]):
                    return result
            if isinstance(left[i], list) and isinstance(right[i], int):
                if result := compare_item(left[i], [right[i]]):
                    return result
            if isinstance(left[i], int) and isinstance(right[i], list):
                if result := compare_item([left[i]], right[i]):
                    return result
        if (i == len(left) - 1) and len(left) < len(right):
            return "yes"


if __name__ == "__main__":
    pairs_input = get_pairs("input.txt")
    indices = compare_pairs(pairs_input)
    print(sum_up_indices(indices))
