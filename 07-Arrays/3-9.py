
list1=["water","book","sky"]  
list2=["water","book","sky"]




def compare(arr1,arr2):
    len1=len(arr1)
    len2=len(arr2)
    if len1 == len2:
        for x in range(len1):
            if arr1[x] == arr2[x]:
                pass
            else:
                return False
        return True




print(compare(list1,list2))