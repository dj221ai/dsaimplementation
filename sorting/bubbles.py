def bubblesort():
    l = [4,2,6,5,1,3]
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    
    print(l)

    max = l[-2]
    print(max)









bubblesort()
