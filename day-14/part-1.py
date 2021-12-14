def main():
    with open('input.txt') as f:
        lines = f.readlines()
        template = lines[0].strip()
        rules = {}
        for line in lines[2:]:
            k, v = line.strip().split(' -> ')
            rules[k] = v
        for i in range(10):
            print(template)
            pairs = []
            for i in range(len(template) -1):
                pairs.append(template[i] + template[i+1])
            new = ''
            for p in pairs:
                new += p[0]
                if p in rules:
                    new += rules[p]
            new += pairs[-1][1]
            template = new
        e = {i for i in template}
        j = sorted([template.count(k) for k in e])
        print()
        print(j)
        print(j[-1] - j[0])

if __name__ == '__main__':
    main()
