from random import randint


def partition3(arr, left, right):
    # write your code here
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
    return low,mid-1

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
