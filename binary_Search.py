def binary_search(arr,item,low,high):
    mid = (low+high)//2

    if high >= low:
       
        if arr[mid] == item:
            return mid
        elif arr[mid] >= item:
            return binary_search(arr,item,low,mid-1)
        else:
            return binary_search(arr,item,mid+1,high)
     
    return -1

arr = list(range(20))
vv = binary_search(arr,10,0,len(arr))
