from math import ceil
def main():
    pairs = {}

    with open('example.txt') as f:
        lines = f.readlines()
        template = lines[0].strip()
        rules = {}
        for line in lines[2:]:
            k, v = line.strip().split(' -> ')
            rules[k] = v
        for i in range(len(template) - 1):
            pairs[template[i] + template[i + 1]] = pairs.get(template[i] + template[i + 1], 0) + 1

        for _ in range(0):
            new_pairs = {}
            print(pairs)
            for pair in pairs:
                if pair in rules:
                    i = pair[0] + rules[pair]
                    j = rules[pair] + pair[1]
                    new_pairs[i] = new_pairs.get(i, 0) + pairs[pair]
                    new_pairs[j] = new_pairs.get(j, 0) + pairs[pair]
                else:
                    new_pairs[pair] = new_pairs.get(pair, 0) + pairs[pair]
            pairs = new_pairs.copy()
        counts = {
            lines[0][0]: 0.5,
            lines[0][-2]: 0.5
        }
        print(pairs)

        for pair in pairs:
            for p in pair:
                counts[p] = counts.get(p, 0) + (pairs[pair] / 2)
        c = sorted(counts.values())
        print(counts)
        print(c[-1] - c[0])
        # can sometimes (most of the time?) give .5, just try either rounding up or down, and it will work
if __name__ == '__main__':
    main()
