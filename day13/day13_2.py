# day13_2.py

from day13_1 import compare_item

DIVIDER1 = [[2]]
DIVIDER2 = [[6]]


def get_packets(filename: str) -> list:
    packets = []
    with open(filename, mode='r') as f:
        for line in f:
            line_stripped = line.strip()
            if line_stripped:
                packet = eval(line_stripped)
                packets.append(packet)
    packets.append(DIVIDER1)
    packets.append(DIVIDER2)
    return packets


def sort_packets(packets: list) -> list:
    for i in range(len(packets)):
        for j in range(len(packets) - i - 1):
            if compare_item(packets[j], packets[j + 1]) == "no":
                temp = packets[j + 1]
                packets[j + 1] = packets[j]
                packets[j] = temp
    return packets


def find_and_multiply_indices(packet_list: list) -> int:
    index1 = packet_list.index(DIVIDER1) + 1
    index2 = packet_list.index(DIVIDER2) + 1
    return index1 * index2


if __name__ == "__main__":
    packets_input = get_packets("input.txt")
    sorted_packets = sort_packets(packets_input)
    print(find_and_multiply_indices(sorted_packets))
