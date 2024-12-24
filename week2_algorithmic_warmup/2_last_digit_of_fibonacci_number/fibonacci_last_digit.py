def fibonacci_last_digit2(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
def fibonacci_last_digit(n):
    last=list()
    last.append(0)
    last.append(1)
    for x in range(2,60):
        temp=last[x-2]+last[x-1]
        last.append(temp%10)
    return last[n%60]
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
