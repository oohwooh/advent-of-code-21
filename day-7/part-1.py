from tqdm import tqdm
def fuel_to_align(crabs, position):
    total_fuel = 0
    for crab in crabs:
        total_fuel += abs(crab - position)
    return total_fuel

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        crabs = []
        for line in lines:
            crabs = [int(c) for c in line.split(',')]
        print(min(fuel_to_align(crabs, crab)for crab in set(crabs)))



if __name__ == '__main__':
    main()
