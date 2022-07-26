# helper function for merging list
def merge(lst1, lst2):
    combined = []
    i=0
    j=0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            combined.append(lst1[i])
            i+=1
        else:
            combined.append(lst2[j])
            j+=1
    
    #if list1 is not empty
    while i<len(lst1):
        combined.append(lst1[i])
        i+=1
    #if list2 is not empty
    while j<len(lst2):
        combined.append(lst2[j])
        j+=1

    return combined


# print(merge([1,2,7,8], [3,4,5,6]))

#dividing the list using recursion until len of list becomes 1
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = int(len(lst)/2)
    left = lst[:mid]
    right = lst[mid:]
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([4,2,6,5,1,3,8]))
