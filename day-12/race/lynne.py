def lynne(lines):
    def create_path(paths, connections, current_path, repeatable):
        options = connections[current_path[-1]]
        options = filter(lambda x: x != 'start' and (
                x.upper() == x or current_path.count(x) == 0 or (x == repeatable and current_path.count(x) <= 1)),
                         options)
        for option in options:
            path = [*current_path, option]
            if option == 'end':
                paths.add(",".join(path))
            else:
                create_path(paths, connections, path, repeatable)

    # list of pairs
    lines = list(map(lambda x: x.strip().split("-"), lines))

    # all cave options
    caves = set(sum(lines, []))

    # set of connections between caves
    connections = {cave: set() for cave in caves}

    # add all connections
    for (a, b) in lines:
        connections[a].add(b)
        connections[b].add(a)

    # set of valid paths
    paths = set()

    # options for going twice
    small_caves = set(filter(lambda x: x.lower() == x and x not in ['start', 'end'], caves))

    # input pairs -- start cave paired with repeatable cave
    sets = []
    for start in connections['start']:
        for cave in small_caves:
            sets.append((start, cave))

    for (option, repeatable) in sets:
        create_path(paths, connections, ['start', option], repeatable)