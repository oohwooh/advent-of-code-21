def main():
    x = 0
    y = 0
    with open('input.txt') as f:
        for line in f.readlines():
            dir, num = line.split(' ')
            num = int(num)
            if dir == 'forward':
                x += num
            if dir == 'down':
                y += num
            if dir == 'up':
                y -= num
        print(x * y)


if __name__ == '__main__':
    main()
