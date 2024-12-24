def fibonacci_number(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a=0
    b=1
    temp=0
    index=0
    while index<n-1:
        temp=a+b
        a=b
        b=temp
        index+=1
    return temp   

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
