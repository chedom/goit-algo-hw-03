import sys

from tower import Tower

def tower_str_format(towers: list[Tower]) -> None:
    towers.sort(key=lambda t: t.name)

    return ", ".join(str(t) for t in towers)

def solve_hanoi_towers(source: Tower, destination: Tower, spare: Tower, num: int) -> None:
    formatted = tower_str_format([source, destination, spare])
    print(f"Intermediate state (depth {num}): {formatted}")

    if num == 0:
        return

    solve_hanoi_towers(source, spare, destination, num-1)
    print(f"Move disk from (depth: {num}) {source.name} to {destination.name}: {num}")
    destination.add_disk(source.pop_disk())
    solve_hanoi_towers(spare, destination, source, num-1)



def parse_args() -> int:
    if len(sys.argv) < 2:
        return 4  # default number of disks

    try:
        order = int(sys.argv[1])
    except ValueError:
        raise ValueError("First argument must be an integer")

    if order <= 0:
        raise ValueError("First argument must be more than zero")

    return order


def main():
    number_of_disks = parse_args()
    # init tower A
    tower_A = Tower("A")
    for i in range(number_of_disks, 0, -1):
        tower_A.add_disk(i)
    # towers B and C are empty
    tower_B, tower_C = Tower("B"), Tower("C")

    formatted = tower_str_format([tower_A, tower_B, tower_C])
    print(f"Initial state: {formatted}")

    solve_hanoi_towers(tower_A, tower_C, tower_B, number_of_disks)


if __name__ == "__main__":
    main()
