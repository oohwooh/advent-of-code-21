def lines_to_counts(lines):
    counts = {}
    for line in lines:
        line = line.strip()
        for idx, char in enumerate(line):
            if idx not in counts:
                counts[idx] = {}
            if char not in counts[idx]:
                counts[idx][char] = 0
            counts[idx][char] += 1
    return counts


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        possible = lines
        i = 0
        known = ''
        while len(possible) > 1:
            counts = lines_to_counts(possible)
            if counts[i].get('0', 0) > counts[i].get('1', 0):
                known += '0'
            else:
                known += '1'
            possible = [k.strip() for k in possible if k.startswith(known)]
            i += 1
        oxygen = possible[0]
        possible = lines
        i = 0
        known = ''
        while len(possible) > 1:
            counts = lines_to_counts(possible)
            if counts[i].get('0', 0) > counts[i].get('1', 0):
                known += '1'
            else:
                known += '0'
            possible = [k.strip() for k in possible if k.startswith(known)]
            print(known, possible)
            i += 1
        co2 = possible[0]
        print(int(oxygen, 2) * int(co2, 2))
if __name__ == '__main__':
    main()
