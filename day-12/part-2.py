``def main():
    def visit_twice_count(k):
        VISITED_TWICE = 0
        for j in k:
            if k.count(j) > 1 and j.islower():
                VISITED_TWICE += 1
        print(VISITED_TWICE)
        return VISITED_TWICE / 2
        # if VISITED_TWICE < 3:
        #     vv.append(k)

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
            return
        bs = connections[path[-1]]
        for b in bs:
            if path.count(b) < 2 or b.isupper():
                if visit_twice_count(path) < 2:
                    if b != 'start':
                        p = path.copy()
                        p.append(b)
                        paths.append(p)
                        branch(p)
    branch(['start'])
    v = [p for p in paths if p[-1] == 'end']
    print(len(v))
    vv = []
    # for k in v:
    def visit_twice_count(k):
        VISITED_TWICE = 0
        for j in k:
            if k.count(j) > 1 and j.islower():
                VISITED_TWICE += 1
        # if VISITED_TWICE < 3:
        #     vv.append(k)


    print(len(vv))

if __name__ == '__main__':
    main()
``