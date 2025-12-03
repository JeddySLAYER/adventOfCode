s = 0

with open("input.txt", "r") as f:
    for i in f :
        i = i.split(',')
        for j in i :
            j = j.split('-')
            for k in range(int(j[0]), int(j[1]) + 1) :
                l = str(k)
                if (l + l).find(l, 1) != len(l) :
                    s += k
    print(s)