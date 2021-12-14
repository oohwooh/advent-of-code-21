def lynne(lines, i):
    template = lines[0]
    instructions = lines[2:]
    rules = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in instructions}

    true_pairs = ["".join(x) for x in zip(template, template[1:])]

    pair_counts = {rule: true_pairs.count(rule) for rule in rules}
    letter_counts = {letter: template.count(letter) for letter in set(template)}
    for _ in range(i):
        new_dict = {rule: 0 for rule in rules}
        for rule in pair_counts:
            if pair_counts[rule] == 0:
                continue
            left_insert = rule[0] + rules[rule]
            right_insert = rules[rule] + rule[1]

            letter_counts.setdefault(rules[rule], 0)
            letter_counts[rules[rule]] += pair_counts[rule]

            new_dict[left_insert] += pair_counts[rule]
            new_dict[right_insert] += pair_counts[rule]

        pair_counts = new_dict

    return max(letter_counts[letter] for letter in letter_counts) - min(
        letter_counts[letter] for letter in letter_counts)