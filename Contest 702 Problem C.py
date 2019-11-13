
def intify(string):
    x = string.split()
    for i in range(len(x)):
        x[i] = int(x[i])
    return x 

def search(item,lst):
    mid = len(lst)//2
    start = 0
    end = len(lst)-1
    while start < end:
        mid = (end+start)//2
        if mid == end or mid == start:
            break
        if item < lst[mid]:
            end = mid
        elif item == lst[mid]:
            return 0
        elif item > lst[mid]:
            start = mid
    if abs(lst[start]-item) < abs(lst[end]-item):
        return abs(lst[start]-item)
    return abs(lst[end]-item)


def evaluate():
    numbers = intify(input())
    cities = intify(input())
    towers = intify(input())
    maxi = 0
    for i in range(len(cities)):
        if maxi < search(cities[i],towers):
            maxi = search(cities[i],towers)
    return maxi

print(evaluate())
    
