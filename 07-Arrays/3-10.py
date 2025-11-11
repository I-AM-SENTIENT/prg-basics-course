def not_appearing(arr1, arr2):
    arr2_set = set(arr2)
    for x in arr1:
        if x not in arr2_set:
            print(x)



list1 = [4,36,12,28,9,44,5]
list2 = [5,1,36]

not_appearing(list1,list2)