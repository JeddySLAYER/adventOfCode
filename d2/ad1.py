s = 0

with open("input.txt", "r") as f:
    for i in f :
        i = i.split(',')
        for j in i :
            j = j.split('-')
            for k in range(int(j[0]), int(j[1]) + 1) :
                l = str(k)
                if (len(l) % 2 == 0) :
                    if ((l[0 : len(l) // 2]) == l[len(l) // 2 :]) :
                        s += k
    print(s)