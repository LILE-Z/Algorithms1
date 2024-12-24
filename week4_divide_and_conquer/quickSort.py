def myQuickSort(A,left,right):
    if left>=right:
        return 
    #Conquer
    m=Partition(A,left,right)
    #Dividing
    myQuickSort(A,left,m-1)
    myQuickSort(A,m+1,right)


def Partition(A,left,right):
    """
    return the index of the final position of the pivot 
    also rearrange in such a way that if its at least pivot
    move them to the left and the with the greatter numbers
    """
    m=A[left]
    j=left
    for i in range(left+1,right+1):
        if A[i]<=m:
            j+=1
            A[i],A[j]=A[j],A[i]
    #Place the pivot
    A[left],A[j]=A[j],A[left]
    return j

arr = [10, 7, 8, 9, 1, 5]
key=Partition(arr,0,len(arr)-1)
print(arr)

myQuickSort(arr,0,len(arr)-1)
print(arr)
