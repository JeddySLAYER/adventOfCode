n = 50
s = 0

with open("input.txt", "r") as f:
    for i in f :
        if i[0] == 'L':
            n -= int(i[1:])
            n = n % 100
            if n == 0 :
                s += 1
        else :
            n += int(i[1:])
            n = n % 100
            if n == 0 :
                s += 1
                
    print(s)