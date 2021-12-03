def main():
    input = []
    with open('input.txt') as f:
        for line in f.readlines():
            input.append(int(line))
    count = 0
    for idx, k in enumerate(input[3:]):
        idx += 2
        j = input[idx] + input[idx-1]
        print(k + j, j + input[idx-2])
        if(k + j > j + input[idx-2]):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
