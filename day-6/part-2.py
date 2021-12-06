def main():
    with open('input.txt') as f:
        lines = f.readlines()
        fish = {key: 0 for key in range(9)}
        print(fish)
        for line in lines:
            fishes = line.split(',')
            for f in fishes:
                fish[int(f)] += 1
        day = 0
        while day < 256:
            temp = {key: 0 for key in range(9)}
            for f in fish:
                temp[f-1] = fish[f]
            reproduce = temp.pop(-1)
            temp[8] += reproduce
            temp[6] += reproduce
            fish = temp
            day += 1
        print(sum(fish[f] for f in fish))


if __name__ == '__main__':
    main()
