def freq(n,l):
    l = [2,3,4,5,6,7,7,7,7,7,7,4,7,6,4,4,2,11,3,43]
    n = len([i for i in l if i == 7])
    return n

#change l value to find exact value

def min(l):
    l = [2,3,4,5,6,7,7,7,7,7,7,4,7,6,4,4,2,11,3,43]
    x=l[0]
    for i in l:
        if i < x:
            x=i
    print(x)

from statistics import mode
l = [2,3,4,5,6,7,7,7,7,7,7,4,7,6,4,4,2,11,3,43]
mode(l)

list = [3, 4, 5,2, 7, 2, 0, 1,-2, 3, 2, 3, 0,3]
print('The list is ' + str(list) + '\n')
print('The frequency of 2 in the list is ' + str(freq(2, list)) +'\n')
print('The minimum value in the list is '+ str(min(list))+ '\n')
print('The mode in the list ' + str(mode(list))+ '\n')