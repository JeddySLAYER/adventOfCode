s = 0    

with open("input.txt", "r") as f:
    for i in f :
        i = i.strip()
        a = []
        b = ''
        for j1 in range(len(i)) :
            for j2 in range(j1 + 1, len(i)) :
                for j3 in range(j2 + 1, len(i)) :
                    for j4 in range(j3 + 1, len(i)) :
                        for j5 in range(j4 + 1, len(i)) :
                            for j6 in range(j5 + 1, len(i)) :
                                for j7 in range(j6 + 1, len(i)) :
                                    for j8 in range(j7 + 1, len(i)) :
                                        for j9 in range(j8 + 1, len(i)) :
                                            for j10 in range(j9 + 1, len(i)) :
                                                for j11 in range(j10 + 1, len(i)) :
                                                    for j12 in range(j11 + 1, len(i)) :
                                                        a.append(int(i[j1] + i[j2] +i[j3] +i[j4] +i[j5] +i[j6] +i[j7] +i[j8] +i[j9] +i[j10] +i[j11] +i[j12]))
        s += (max(a))
        
    print(s)