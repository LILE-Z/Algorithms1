from itertools import permutations



def largest_number_naive(numbers):
    print(numbers)
    numbers = list(map(str, numbers))
    print(numbers)
    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


# def bestOption(numbers,maxL):
#     index_Best=0  
#     bestNumber=-1
#     for index in range(len(numbers)):
#         temp=0
#         if numbers[index]=='0':continue
#         if maxL > len(numbers[index]):
#             temp=int(numbers[index]+(numbers[index][-1] * (maxL - len(numbers[index]))))
#         else:
#             temp=int(numbers[index])
#         if temp>bestNumber:
#             bestNumber=temp
#             index_Best=index
#     return index_Best
#
#
# def largest_number_greedy1(numbers):
#     digits=len(max(numbers,key=lambda x: len(x)))
#     
#     bestIndex=0
#     result=''
#     for x in  range(len(numbers)):      
#         bestIndex=bestOption(numbers,digits)
#         result+=numbers[bestIndex]
#         numbers[bestIndex]='0'
#     return result
#

def bestOption(numbers):
    bestIndex=0
    for x in range(len(numbers)):
        if numbers[x]=='0':
            continue
        if int(numbers[x]+numbers[bestIndex])>int(numbers[bestIndex]+numbers[x]):
            bestIndex=x
    return bestIndex

def largest_number_greedy(numbers):
    number=''
    for x in range(len(numbers)):
        index=bestOption(numbers)
        number+=(numbers[index])
        numbers[index]='0'
    return number


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_greedy(input_numbers))
