def insertion():
    # l = [4,2,6,5,1,3]
    l = [1,2,4,3,5,6]
    for i in range(1, len(l)):
        temp = l[i]
        j = i-1
        while temp < l[j] and j > -1:
            l[j+1] = l[j]
            l[j] = temp
            j -= 1
    print(l)


insertion()
