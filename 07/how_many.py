#finds frequency of numbers in the list
def freq(n, l):
    count = 0
    for i in l:
        if i == n:
            count += 1
        return count
#finds minimum value in list
    def min(l):
        min = l[0]
        for i in l:
            if i < min:
                min = i
        return min
#finds mode in list
    def mode(l):
        v = []
        
        for i in l:
            v.append(freq(i, l))
        mode = v[i]
        for i in v:
            if mode < v[i]:
                mode = l[i]
        return mode
    
list = [2, 4, 5, 1, 6, 5, 9, 2, 1, 3, 7, 6, 8, 5,]
print('The list is ' + str(list) + '\n')
print('The frequency of 2 in the list is ' + str(freq(2, l))