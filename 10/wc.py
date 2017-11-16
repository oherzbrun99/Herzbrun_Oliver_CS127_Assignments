def remove_non_alpha(w):
    """
    input: w - string representing a "word"
    output: the string with non alpha chars removed
    """
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result


def bwcd(wordlist):
    d={}
    """
    input: w - list of words
    output: dictionary of Freq of times key value appears
    """
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1



def mak_chain(f):
    """
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
             of words that come after key
    """
    text = open(f).read()
    w_list = text.split()
    d = {}
    for i in range(len(w_list)):
        w = remove_non_alpha(w_list[i].lower())
        d.setdefault(w,[])
        if (i != len(w_list)-1):
            hold = d[w]
            hold.append(remove_non_alpha(w_list[i+1]).lower())
            d[w]=hold
    return d


d = mak_chain("hamlet.txt")
print(d)


