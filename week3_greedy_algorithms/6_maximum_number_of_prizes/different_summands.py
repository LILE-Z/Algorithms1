def optimal_summands(n):
    summands = []
    remaining=n
    number=0
    if n==1 or n==2:return [n]
    while remaining>0:
    #If the number can make numero+2 the that means we have to return all the remaining
        if number+1<remaining and   remaining-(number+1)>=number+2:
            number+=1
            summands.append(number)
            remaining-=(number)
        else:
            summands.append(remaining)
            remaining-=remaining
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
