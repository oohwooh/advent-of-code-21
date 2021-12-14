def lola(lines, i):
    pairs = {}
    template = lines[0]
    rules = {}
    for line in lines[2:]:
        k, v = line.split(' -> ')
        rules[k] = v
    for i in range(len(template) - 1):
        pairs[template[i] + template[i + 1]] = pairs.get(template[i] + template[i + 1], 0) + 1

    for _ in range(i):
        new_pairs = {}
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
        lines[0][-1]: 0.5
    }

    for pair in pairs:
        for p in pair:
            counts[p] = counts.get(p, 0) + (pairs[pair] / 2)
    c = sorted(counts.values())
