def ThreeWayPartition(arr,left,right):
    """
    return m1 and m2 ,
    where
    m1 is the boundery between those numbers less than the pivot
    m2 is the boundery  between higer and equal
    """
    mid=left
    low=left
    high=right
    pivot=arr[left]
    while mid <= high:
        #Low
        if arr[mid]<pivot:
            arr[mid],arr[low]=arr[low],arr[mid]
            mid+=1
            low+=1
        #Middle
        elif arr[mid]==pivot:
            mid+=1
        #Higher
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
                #Because we dont know the content of arr[high] initily we dont increase mid
            high-=1
        print(arr)
    print(arr[low])
    print(arr[mid-1])
arr=[2,1,1,1,2,2,3,3,1,3,2]
ThreeWayPartition(arr,0,len(arr)-1)
