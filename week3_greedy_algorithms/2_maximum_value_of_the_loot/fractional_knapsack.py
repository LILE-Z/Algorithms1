from sys import stdin

def Best_Option(weights,values):
    bestIndex=0
    bestValue=0
    for i,value in enumerate(values):
        if weights[i]>0 and (value/weights[i]) > bestValue:
            bestValue=value/weights[i]
            bestIndex=i
    return bestIndex

def min_weight(weight,capacity):
    #"Takes the maximum amount of weight depending of remaining capacity"
    if capacity<=weight:
        return capacity
    if capacity>weight:
        return weight

def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    for index in range(len(values)):
        if capacity==0:
            return value
        i=Best_Option(weights,values)
        a=min_weight(weights[i],capacity)
        value+=(a*(values[i]/weights[i]))
        weights[i]-=a
        capacity-=a
    return value

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
