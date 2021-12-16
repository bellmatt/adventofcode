from dataclasses import dataclass
import dataclasses
from typing import List


@dataclass
class Packet:
    packet_version: int
    packet_type_id: int
    binary: str


@dataclass
class LiteralValue(Packet):
    value: int


@dataclass
class Operator(Packet):
    sub_packets: List[Packet]


@dataclass
class BITS:
    hex: str
    binary: str
    packet: Packet

    def __init__(self, hex: str):
        self.hex = hex
        self.binary = f"{int(hex, 16):0>{len(hex)*4}b}"
        # print(self.binary)
        i = 0
        self.packet = parse_packet(self.binary[i:])
        print(self.packet)


def parse_packet(binary: str) -> Packet:
    i = 0
    # header
    packet_version = int(binary[i : i + 3], 2)
    packet_type_id = int(binary[i + 3 : i + 6], 2)

    if packet_type_id == 4:
        # Literal value
        value_binary_str = ""
        # Look in increments of 5 from current value from i to find value
        for j in range(i + 6, len(binary), 5):
            if list(binary)[j] == "1":
                value_binary_str += binary[j + 1 : j + 5]
            else:
                # last group, ignore rest of the string
                value_binary_str += binary[j + 1 : j + 5]
                break
        j += 5
        packet = LiteralValue(
            packet_version, packet_type_id, binary[i:j], int(value_binary_str, 2)
        )
        return packet
    else:
        # operator
        # header + Length type ID
        packet_length = 7
        sub_packets = []
        if binary[i + 6] == "0":
            # next 15 bits are the length of the sub packets
            sub_packets_length = int(binary[i + 7 : i + 22], 2)
            packet_length += 15 + sub_packets_length
            l = 0
            while l < sub_packets_length - 1:
                new_packet = parse_packet(binary[i + 22 + l : i + packet_length])
                l += len(new_packet.binary)
                sub_packets.append(new_packet)
        else:
            # next 11 bits are the number of sub packets
            packet_length += 11
            num_sub_packets = int(binary[i + 7 : i + 18], 2)
            for n in range(num_sub_packets):
                new_packet = parse_packet(binary[i + packet_length :])
                packet_length += len(new_packet.binary)
                sub_packets.append(new_packet)
        packet = Operator(
            packet_version, packet_type_id, binary[i : i + packet_length], sub_packets
        )
    return packet


def version_sum(packet: dict) -> int:
    total = 0
    total += packet["packet_version"]
    if packet["packet_type_id"] != 4:
        for sub in packet["sub_packets"]:
            total += version_sum(sub)
    return total


if __name__ == "__main__":
    input = open("./src/day16_input.txt", "r").readline().rstrip()
    # input = "D2FE28"
    # input = "38006F45291200"
    # input = "EE00D40C823060"
    # input = "8A004A801A8002F478"
    # input = "620080001611562C8802118E34"
    # input = "C0015000016115A2E0802F182340"
    # input = "A0016C880162017C3686B18A3D4780"
    transmission = BITS(input)
    print(version_sum(dataclasses.asdict(transmission.packet)))
