truth_table = {
    0: ['a', 'b', 'c', 'd', 'e', 'f'],
    1: ['b', 'c'],
    2: ['a', 'b', 'd', 'e', 'g'],
    3: ['a', 'b', 'c', 'd', 'g'],
    4: ['b', 'c', 'f', 'g'],
    5: ['a', 'c', 'd', 'f', 'g'],
    6: ['a', 'c', 'd', 'e', 'f', 'g'],
    7: ['a', 'b', 'c'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'f', 'g']
}

def main():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            input, output = line.split(' | ')
            input = input.split(' ')
            output = output.split(' ')
            known = {}
            one = [i for i in input if len(i) == 2][0]
            four = [i for i in input if len(i) == 4][0]
            seven = [i for i in input if len(i) == 3][0]
            eight = [i for i in input if len(i) == 7][0]
            three = [i for i in input if len(i) == 5 and all(j in i for j in one)][0]
            nine = [i for i in input if len(i) == 6 and all(j in i for j in three)][0]
            zero = [i for i in input if len(i) == 6 and all(j in i for j in seven) and i != nine][0]
            six = [i for i in input if len(i) == 6 and i != nine and i != zero][0]
            five = [i for i in input if len(i) == 5 and all(j in nine for j in ''.join([i, three])) and i != three][0]
            two = [i for i in input if len(i) == 5 and i != five and i != three][0]
            if(three == five):
                print('cringe')

            known = {
                ''.join(sorted(one)): 1,
                ''.join(sorted(two)): 2,
                ''.join(sorted(three)): 3,
                ''.join(sorted(four)): 4,
                ''.join(sorted(five)): 5,
                ''.join(sorted(six)): 6,
                ''.join(sorted(seven)): 7,
                ''.join(sorted(eight)): 8,
                ''.join(sorted(nine)): 9,
                ''.join(sorted(zero)): 0
            }
            print(known)
            out = []
            for o in output:
                out.append(str(known[''.join(sorted(o))]))
            total += int(''.join(out))
    print(total)
if __name__ == '__main__':
    main()
