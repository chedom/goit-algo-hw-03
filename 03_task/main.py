import sys

from tower import Tower


def solve_hanoi_towers(source: Tower, destination: Tower, spare: Tower, num: int) -> None:
    towers = [source, destination, spare]
    towers.sort(key=lambda t: t.name)

    for t in towers:
        print(str(t))

    if num == 0:
        return

    num -= 1

    solve_hanoi_towers(source, spare, destination, num)
    print(f"Move disk from {source.name} to {destination.name}")
    destination.add_disk(source.pop_disk())
    solve_hanoi_towers(spare, destination, source, num)


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
    tower_A = Tower("A", number_of_disks)
    for i in range(number_of_disks, 0, -1):
        tower_A.add_disk(i)
    # towers B and C are empty
    tower_B, tower_C = Tower("B", number_of_disks), Tower("C", number_of_disks)

    solve_hanoi_towers(tower_A, tower_C, tower_B, number_of_disks)


if __name__ == "__main__":
    main()
