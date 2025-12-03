n = 50
s = 0

with open("input.txt", "r") as f:
    for i in f :
        j = int(i[1:])
        k = j - (j % 100)
        s += k // 100
        if i[0] == 'L':
            if n != 0 :
                n -= (j % 100)
                if n <= 0 :
                    s += 1
            else :
                n -= (j % 100)
            n = n % 100
        else :
            if n != 0 :
                n += (j % 100)
                if n >= 100 :
                    s += 1
            else :
                n += (j % 100)
            n = n % 100
                
    print(s)