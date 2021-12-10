open_chars = ['(', '[', '{', '<']
close_chars = [')', ']', '}', '>']
import statistics

def is_line_corrupted(line):
    layout = {}
    level = 0
    for char in line:
        if char in open_chars:
            level += 1
            layout.setdefault(level, [])
            layout[level].append(char)
        o = None
        if char in close_chars:
            for idx, c in enumerate(close_chars):
                if c == char:
                    o = open_chars[idx]
            layout.setdefault(level, [])
            if o not in layout[level]:
                return True
            else:
                layout[level].remove(o)
            layout[level].append(char)
            level -= 1
    return False


def is_line_complete(line):
    layout = {}
    level = 0
    for char in line:
        if char in open_chars:
            level += 1
            layout.setdefault(level, [])
            layout[level].append(char)
        o = None
        if char in close_chars:
            for idx, c in enumerate(close_chars):
                if c == char:
                    o = open_chars[idx]
            layout.setdefault(level, [])
            if o not in layout[level]:
                return False
            else:
                layout[level].remove(o)
            level -= 1
    return all(len(layout[level]) == 0 for level in layout), layout

def lola(lines):
    sols = []
    error_score = 0
    for line in lines:
        sol = ''
        if not is_line_corrupted(line):
            layout = is_line_complete(line)[1]
            for i in sorted(layout, reverse=True):
                if len(layout[i]) == 0:
                    pass
                else:
                    o = None
                    for idx, c in enumerate(open_chars):
                        if c == layout[i][0]:
                            o = close_chars[idx]
                    sol += o
            sols.append(sol)
    scores = []
    for sol in sols:
        score = 0
        for char in sol:
            score *= 5
            if char == ')':
                score += 1
            if char == ']':
                score += 2
            if char == '}':
                score += 3
            if char == '>':
                score += 4
        scores.append(score)
    scores.sort()
    return statistics.median(scores)
