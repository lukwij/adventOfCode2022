# day4_2.py

from day4_1 import get_next_elf_pair, get_cleaning_areas


def do_areas_overlap(area1, area2) -> bool:
    if area1[0] <= area2[0]:
        if area1[1] >= area2[0]:
            return True
    if area1[0] >= area2[0]:
        if area1[0] <= area2[1]:
            return True
    return False


if __name__ == "__main__":
    overlap_count = 0
    for elf_pair in get_next_elf_pair("input.txt"):
        area_pair = get_cleaning_areas(elf_pair)
        if do_areas_overlap(area_pair[0], area_pair[1]):
            overlap_count += 1
    print(f"Total score: {overlap_count}")
