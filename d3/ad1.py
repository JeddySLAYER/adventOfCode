s = 0

with open("input.txt", "r") as f:
    for i in f :
        i = i.strip()
        a = []
        b = ''
        for j in range(len(i)) :
            for k in range(j + 1, len(i)) :
                a.append(int(i[j] + i[k]))
        s += (max(a))
        
    print(s)