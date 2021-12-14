def main():
    connections = {}
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            s, e = line.split('-')
            connections.setdefault(s, [])
            connections.setdefault(e, [])
            connections[s].append(e)
            connections[e].append(s)
    paths = []
    def branch(path):
        if path[-1] == 'end':
            print(path)
            return
        bs = connections[path[-1]]
        for b in bs:
            print(b)
            if b not in path or b.isupper():
                p = path.copy()
                p.append(b)
                paths.append(p)
                branch(p)
    branch(['start'])
    print(len([p for p in paths if p[-1] == 'end']))

if __name__ == '__main__':
    main()
