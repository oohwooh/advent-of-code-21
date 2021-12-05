def check_win(board, called):
    for row in board:
        if all([num in called for num in row]):
            print('row is winner!')
            return True
    for i in range(5):
        col = []
        for row in board:
            col.append(row[i])
        if all([num in called for num in col]):
            print('col is winner!')
            return True

def all_unmarked_numbers(board, called):
    ret = []
    for row in board:
        for num in row:
            if num in called:
                pass
            else:
                ret.append(int(num))
    return ret


def main():
    boards = []
    called = []
    with open('input.txt') as f:
        lines = f.readlines()
        to_call = lines[0].split(',')
        tempboard = []
        for line in lines[1:]:
            line = line.strip()
            row = line.split(" ")
            if len(row) == 1:
                if tempboard != []:
                    boards.append(tempboard)
                tempboard = []
            else:
                tempboard.append([r for r in row if r != ''])
        print(boards)
        for call in to_call:
            print('calling', call)
            called.append(call)
            for board in boards:
                if check_win(board, called):
                    print(sum(all_unmarked_numbers(board, called)) * int(call))
                    break

if __name__ == '__main__':
    main()
