def main():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            input, output = line.split(' | ')
            input = input.split(' ')
            output = output.split(' ')
            for out in output:
                if len(out) in [2, 3, 4, 7]:
                    total += 1
                    print(out)
    print(total)


if __name__ == '__main__':
    main()
