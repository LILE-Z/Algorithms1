def max_pairwise_product(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
