from dataclasses import dataclass


@dataclass
class Position:
    name: str
    long: float = 0.0
    lat: float = 0.0


if __name__ == "__main__":
    here = Position("here")
    there = Position("there", 34.6, 3.5)
    print(there)
    print(here == there)
