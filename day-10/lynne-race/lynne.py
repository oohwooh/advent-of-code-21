def lynne(inp):
    lines = list(map(lambda x: x.strip(), inp))
    # score values for part 1
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    start = "([{<"
    end = ")]}>"
    # score values for part 2 (via index)
    auto_points = " )]}>"
    # score for part 1
    score = 0
    # scores for part 2
    auto_scores = []

    for line in lines:
        if line[0] in end:
            raise ValueError("Illegal starting " + line[0])
        # list of ending characters the processor expects to find
        to_find = [end[start.index(line[0])]]
        # set to True when a chunk is corrupt
        br = False
        for char in line:
            if char in start:
                i = start.index(char)
                to_find.append(end[i])
            else:
                i = end.index(char)
                if char != to_find[-1]:
                    score += scores[char]
                    br = True
                    break
                else:
                    # we found the right ending character
                    to_find.pop()
        # skip autocompletion of corrupt chunks
        if br: continue
        # get rid of first to autocomplete (i don't know why but it works)
        to_find = to_find[1:]
        completion_string = "".join(reversed(to_find))
        # autocomplete score
        sc = 0
        for c in completion_string:
            sc *= 5
            # grab point value as index of character
            sc += auto_points.index(c)
        auto_scores.append(sc)
    auto_scores.sort()
    # print("Part 1:", score)
    return auto_scores[len(auto_scores)//2]