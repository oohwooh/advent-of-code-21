def main():
    with open('input.txt') as f:
        lines = f.readlines()
        fish = []
        for line in lines:
            fishes = line.split(',')
            for f in fishes:
                fish.append(int(f))
        day = 0
        while day < 80:
            print(fish)
            for idx, f in enumerate(fish):
                fish[idx] -= 1
                if f == 0:
                    fish.append(9)
                    fish[idx] = 6
            day += 1
        print(len(fish))


if __name__ == '__main__':
    main()
