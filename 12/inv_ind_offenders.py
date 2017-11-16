
import csv, string

death_row = open('offenders-clean.csv')

def search(a):
    read = csv.reader(a)
    data = list(read)
    newdata = []
    mydict = {}
    for i in range(1, len(data)):
        newdata.append([data[i][0], data[i][8]])
    for k, v in newdata:
        v = v.split()
        for word in v:
            word = word.translate(string.punctuation)
            mydict.setdefault(word, [])
            if word not in mydict:
                mydict[word] = k
            else:
                mydict[word].append(k)
    return mydict

print(search(death_row))