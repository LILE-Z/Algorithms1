from sys import stdin


def min_refills2(distance, tank, stops):
    '''
    Plan
    1.Create segments, that represents the tank autonomy
    2.Move across the array to find the last stop inside or segment
   '''
    covered=tank
    left=0
    right=0
    counter=0
    while covered<distance:
        left=right
        #Distance between stops
        while right<len(stops)-1 and stops[right+1]<covered:
                right+=1
                
        if right==left:
            return -1
        covered=stops[right]+tank
        counter+=1
    return counter
def min_refills(distance,tank,stops):
    stops=[0]+stops+[distance]
    current=0
    last=0
    counter=0
    while current<len(stops)-1:
        
        last=current
        while current<len(stops)-1 and stops[current+1]-stops[last]<=tank:
            current+=1
        #if current doesnt change that means that in never went into the loop
        if current==last:
            return -1 #Impossible to reach the next stop with the availble fuil
        if current<len(stops)-1: counter+=1 #The inner loop could create a current out of range 
    #If we could reach the last stop "the end" that means we could achive our goal
    return counter



if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    # d=500
    # m=200
    # stops=[100,200,300,400]
    print(min_refills(d, m, stops))
