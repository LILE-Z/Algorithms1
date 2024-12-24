# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if from_==0 and to==1:return to
    if from_==0 and to==0: return to
    previous=0
    current=1
    
    #Find the position in the pattern
    from_=((from_)%60)
    to=((to)%60)
        
    #Store value
    val=0
    #Consider the first elemment
    if from_==0 or from_==1:
        val+=1
    #Bug what happen when to after %10 is less than from_ 
    if to<from_:
        to+=60 #We add 1 more round , that way we get to over from
    

    for position in range(2,to+1):
        aux=previous+current
        previous=current
        current=aux%10
        if position>=from_  :
            val+=current        
    return val%10
if __name__ == '__main__':
    input_str = input()
    from_, to = map(int, input_str.split())
    print(fibonacci_partial_sum_naive(from_, to))
