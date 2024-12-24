import random
def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1
    return 0

def majority_element(elements):
    #Conquer
    if len(elements)==1:
        return elements[0]
    
    
    #Dividing
    half=len(elements)//2
    best1=majority_element(elements[:half])
    best2=majority_element(elements[half:])
    
    #Merging
    #Actually the procces of mergin is basically taking elements= [:half] + [half:]
    
    #Conquer 2
    if best1==0 and best2==0:return 0
    
    
    times1=elements.count(best1)
    if best1==best2:
        if times1>len(elements)/2:
            return best1 
        else:
            return 0
    
    times2=elements.count(best2)

    if times2>len(elements)/2:
        return best2
    if times1>len(elements)/2:
        return best1
    return 0

#Data generator
def dataGen():
    return [random.randint(1,10000) for x in range(random.randint(1,10))]
    



def test():
    value1,value2=0,0
    while value1==value2:
        dataSet=dataGen()
        print(dataSet)
        value1=majority_element_naive(dataSet)
        value2=majority_element(dataSet)
        if value2>0:value2=1
        print("val1= {0} val2={1}".format(value1,value2))


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
  #  print(majority_element_naive(input_elements))
   # print("my")
    if majority_element(input_elements)>0:print(1)
    else:print(0)
