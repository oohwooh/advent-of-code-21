def main():
    input = []
    with open('input.txt') as f:
        for line in f.readlines():
            input.append(int(line))
    count = 0
    for idx, k in enumerate(input[1:]):
        if(k > input[idx]):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
