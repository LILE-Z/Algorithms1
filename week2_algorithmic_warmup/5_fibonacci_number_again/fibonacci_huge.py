def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
def fibonacci_huge(n,m):
    
    arr=[0,1]
    previous=0
    current=1
    if n==0:return arr[0]
    if n==1:return arr[1]
    """
    in the if means that the next iteration would be the start of
    a pissaono period
    """
    for x in range(n-1):
        temp=current+previous
        previous=current
        current=temp%m
        arr.append(current)
        if previous==0 and current==1:
            index=n%(x+1)
            return arr[index]
    #If n is small , and doesnt reach a pissano period you should return the current
    return current
if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
