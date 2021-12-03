def main():
    horiz = 0
    depth = 0
    aim = 0
    with open('input.txt') as f:
        for line in f.readlines():
            dir, num = line.split(' ')
            num = int(num)
            if dir == 'forward':
                horiz += num
                depth += (aim*num)
            if dir == 'down':
                aim += num
            if dir == 'up':
                aim -= num
        print(horiz * depth)

if __name__ == '__main__':
    main()
