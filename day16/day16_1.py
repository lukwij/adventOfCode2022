# day16_1.py

import re
import logging


def build_net(filename: str) -> list:
    valve_net = []
    with open(filename, mode='r') as f:
        for line in f:
            logging.info(f"Incoming data: {line.strip()}")
            result = re.search(r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line.strip())
            logging.info(result.groups())
            valve_info = {
                "name": result[1],
                "flow": result[2],
                "connections": result[3].split(", ")
            }
            logging.info(valve_info)
            valve_net.append(valve_info)
    return valve_net





if __name__ == "__main__":
    # logging.basicConfig(filename="valve.log", filemode="w", level=logging.INFO)
    logging.basicConfig(level=logging.INFO)
    build_net("sample.txt")