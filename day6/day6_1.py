# day6_1.py


def get_datastream(filename: str) -> str:
    with open(filename, mode='r') as f:
        for character in f.readline():
            yield character


def find_first_marker(filename: str, buffer_size: int) -> int:
    first_marker_position = 0
    small_buffer = []
    for character in get_datastream(filename):
        first_marker_position += 1
        small_buffer.append(character)
        if buffer_size == len(small_buffer):
            if len(set(small_buffer)) < buffer_size:
                del small_buffer[0]
            else:
                return first_marker_position


def first_start_of_packet_marker():
    print(find_first_marker("input.txt", 4))


if __name__ == "__main__":
    first_start_of_packet_marker()
