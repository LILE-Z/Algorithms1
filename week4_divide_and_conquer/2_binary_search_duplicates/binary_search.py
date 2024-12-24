def binary_search1(keys, query):
    l=0
    r=len(keys)-1
    while l<=r:
        half=(l+r)//2
        if query==keys[half]:
            if half-1>=0:
                better=binary_search(keys[:half],query)
                if better != -1:
                    return better
                else:
                    return half
            else:return half
        if query<keys[half]:
            r=half-1
        else:
            l=half+1
    return -1




def binary_search(keys,query,l,r):
    if l>r:
        return -1
    half=(l+r)//2
    if query==keys[half]:
        if half-1>=0 and keys[half-1]==query:
            better=binary_search(keys,query,l,half)
            if better != -1:
                return better
            else:
                return half
        else:return half
    if query<keys[half]:
        return binary_search(keys,query,l,half-1)
    else :
        return binary_search(keys,query,half+1,r)



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries
    l=0
    r=len(input_keys)-1
    for q in input_queries:
        print(binary_search(input_keys, q,l,r), end=' ')
