def main():
    dots = {}
    folds = []
    max_x = 0
    max_y = 0
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('fold'):
                x_or_y, n = line.split(' ')[2].split('=')
                folds.append((x_or_y, int(n)))
            else:
                x, y = line.split(',')
                x = int(x)
                y = int(y)
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y
                dots[x, y] = True
    print(dots)
    for fold in folds:
        for dot in dots.copy():
            x, y = dot
            if fold[0] == 'y':
                if y > fold[1]:
                    dots[x, y] = False
                    dots[x, fold[1] - abs(y - fold[1])] = True
            else:
                if x > fold[1]:
                    dots[x, y] = False
                    dots[fold[1] - abs(x - fold[1]), y] = True
    d = [dot for dot in dots if dots[dot] == True]
    max_x = 0
    max_y = 0
    for x, y in d:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    for y in range(max_y + 1):
        out = ''
        for x in range(max_x + 1):
            if dots.get((x, y)):
                out += '#'
            else:
                out += '.'
        print(out)
    print(len(d))
if __name__ == '__main__':
    main()
