from tqdm import tqdm
def fuel_to_align(crabs, position):
    total_fuel = 0
    for crab in crabs:
        steps = abs(crab - position)
        total_fuel += steps * (steps + 1) / 2
    return total_fuel

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        crabs = []
        for line in lines:
            crabs = [int(c) for c in line.split(',')]
        print(min(fuel_to_align(crabs, crab)for crab in range(max(crabs))))


if __name__ == '__main__':
    main()
