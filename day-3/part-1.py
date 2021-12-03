def main():
    with open('input.txt') as f:
        counts = {}
        gamma = ''
        epsilon = ''
        for line in f.readlines():
            line = line.strip()
            for idx, char in enumerate(line):
                if idx not in counts:
                    counts[idx] = {}
                if char not in counts[idx]:
                    counts[idx][char] = 0
                counts[idx][char] += 1
        for bit in counts:
            bit = counts[bit]
            print(bit)
            if bit['0'] > bit['1']:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'
        print(int(gamma, 2) * int(epsilon, 2))


if __name__ == '__main__':
    main()
