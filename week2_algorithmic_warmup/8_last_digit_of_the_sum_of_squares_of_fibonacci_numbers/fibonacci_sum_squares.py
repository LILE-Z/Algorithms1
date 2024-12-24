def fibonacci_sum_squares_Naive(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10
def fibonacci_sum_squares(n):
    if n<=1:
        return n
    n%=60
    #Formula
    height=0
    
    
    previous=0
    current=1

    for times in range(2,n+2):
        previous,current=current,(previous+current)%10
        if times==n:
            height=current
    return (current*height)%10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
