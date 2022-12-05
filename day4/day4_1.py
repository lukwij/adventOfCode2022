# day5_1.py

def get_next_elf_pair(filename: str) -> str:
    with open(filename, mode='r') as f:
        for line in f:
            yield line.strip()


def get_cleaning_areas(pair: str) -> [tuple]:
    area1 = pair.split(",")[0]
    area2 = pair.split(",")[1]
    area1_start = int(area1.split("-")[0])
    area1_end = int(area1.split("-")[1])
    area2_start = int(area2.split("-")[0])
    area2_end = int(area2.split("-")[1])
    return [(area1_start, area1_end), (area2_start, area2_end)]


def do_areas_fully_overlap(area1, area2) -> bool:
    if area1[0] <= area2[0]:
        if area1[1] >= area2[1]:
            return True
    if area1[0] >= area2[0]:
        if area1[1] <= area2[1]:
            return True
    return False


if __name__ == "__main__":
    overlap_count = 0
    for elf_pair in get_next_elf_pair("input.txt"):
        area_pair = get_cleaning_areas(elf_pair)
        if do_areas_fully_overlap(area_pair[0], area_pair[1]):
            overlap_count += 1
    print(f"Total score: {overlap_count}")
