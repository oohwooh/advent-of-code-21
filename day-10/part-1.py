def main():
    open_chars = ['(', '[', '{', '<']
    close_chars = [')', ']', '}', '>']
    with open('input.txt') as f:
        lines = f.readlines()
        error_score = 0
        for line in lines:
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
                        print(f'Found {char} instead')
                        if char == ')':
                            error_score += 3
                        if char == ']':
                            error_score += 57
                        if char == '}':
                            error_score += 1197
                        if char == '>':
                            error_score += 25137
                        break
                    else:
                        layout[level].remove(o)
                    layout[level].append(char)
                    level -= 1

        #         if char == '(':
        #             parenth += 1
        #         if char == '[':
        #             square += 1
        #         if char == '{':
        #             curl += 1
        #         if char == '<':
        #             point += 1
        print(error_score)
        # print(layout)


if __name__ == '__main__':
    main()
