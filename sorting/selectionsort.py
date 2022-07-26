def selection():
    l = [4,2,6,5,1,3]

    for i in range(len(l)-1):
        minidx = i
        for j in range(i+1, len(l)):
            if l[j] < l[minidx]:
                minidx = j
        if i!=minidx:
            temp = l[i]
            l[i] = l[minidx]
            l[minidx] = temp

    print(l)


selection()
