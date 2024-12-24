def change(money):
    """
   Minimum number of coins needed to change the give value into  
    1,5 and 10
    """
    change=0  
    if money>=10:
        change+= (money//10)
        money-=(10*(money//10))
    if money>=5:
        change+=(money//5)
        money-=(5*(money//5))
    if money>=1:
        change+=(money)
    return change


if __name__ == '__main__':
    m = int(input())
    print(change(m))
