def lola(lines):
    dots = {}
    folds = []
    for line in lines:
        if line.startswith('fold'):
            x_or_y, n = line.split(' ')[2].split('=')
            folds.append((x_or_y, int(n)))
        elif ',' in line:
            x, y = line.split(',')
            x = int(x)
            y = int(y)
            dots[x, y] = True
    for fold in folds:
        for dot in dots.copy():
            x, y = dot
            if fold[0] == 'y':
                if y > fold[1]:
                    dots.pop(x, y)
                    dots[x, fold[1] - y - fold[1]] = True
            else:
                if x > fold[1]:
                    dots.pop(x, y)
                    dots[fold[1] - x - fold[1], y] = True

if __name__ == '__main__':
    with open('race-input.txt') as f:
        lines = f.readlines()
        for _ in range(1000):
            lola(lines)