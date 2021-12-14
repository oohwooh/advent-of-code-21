def filter_options(options, current_path):
    small = len([1 for a in current_path if a.upper() != a])
    if small > 1:
        options = filter(lambda a: a.upper() == a, options)
    return list(options)

def create_path(connections, current_path):
    print(current_path)
    options = connections[current_path[-1]]
    for connection in options:
        options = filter_options(options, [*current_path, connection])
        print(current_path, options)
        if len(options) <= 1:
            # print(current_path)
            pass
        else:
            for conn in options:
                create_path(connections, [*current_path, connection, conn])

with open("example.txt") as inp:
    lines = list(map(lambda x: x.strip().split("-"), inp.readlines()))
    caves = set(sum(lines, []))

    connections = {cave: set() for cave in caves}
    for line in lines:
        a, b = line
        connections[a].add(b)
        connections[b].add(a)
    paths = []
    create_path(connections, ['start'])