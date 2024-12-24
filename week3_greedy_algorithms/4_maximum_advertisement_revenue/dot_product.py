from itertools import permutations


def max_dot_product2(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product
def max_dot_product(first_sequence,second_sequence):
    first_sequence.sort()
    second_sequence.sort()
    return sum(first_sequence[i] * second_sequence[i] for i in range(len(first_sequence)))
def max_dot_productGreedy(first_sequence,second_sequence):
    
    def best_Option(array):
        """Return the index of the highes number available in the array"""
        bestIndex=0
        n=len(array)
        for index in range(n):
            if array[index]>array[bestIndex]:
                bestIndex=index
        return bestIndex
    
    n=len(first_sequence)
    result=0
    for i in range(n):
        indexFirst=best_Option(first_sequence)
        indexSecond=best_Option(second_sequence)
        result+=(first_sequence[indexFirst]*second_sequence[indexSecond])
        first_sequence[indexFirst]=0
        second_sequence[indexSecond]=0
    return result
if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
