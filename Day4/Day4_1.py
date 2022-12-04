with open('input.txt', 'r') as f:
    pairs = f.readlines()
    total = 0
    for p in pairs:
        p = p.strip()
        l = []
        r = []
        left = []
        right = []
        p = p.split(',')
        l = p[0].split('-')
        r = p[1].split('-')
        for n in range(int(l[0]), int(l[1])+1):
            left.append(n)
        for n in range(int(r[0]), int(r[1])+1):
            right.append(n)
        if set(left).issubset(set(right)) or set(right).issubset(set(left)):
            total += 1
    print(total)