def fibonacci_sum(n):
    if n <= 1:
        return n
    arr=[0,1]
    previous=0
    current=1
    for x in range(60):
        aux=current+previous
        previous=current
        current=aux%10
        arr.append(current)
    res=arr[(n+2)%60]-1
    #That means that we are returning from the last position 10 mod 10 =0
    # 1 position =9
    if res== -1:
        return 9
    return res

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
    
