import random

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
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1
    return d

def build_word_chain_dict(wordlist):
    d={}
    for i in range(1,len(wordlist)):
        w1 = wordlist[i-1]
        w2 = wordlist[i]
        d.setdefault(w1,[])
        d[w1].append(w2)

    return d



def bwcff(f):
    """
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
             of the number of times each word occursb
    """
    text = open(f).read()
    l=[]
    for w in text.split():
        w = w.lower()
        w = remove_non_alpha(w)
        l.append(w)
    d = build_word_chain_dict(l)
    return d

def build_trigram(file):
    text = open(file).read()
    ret_dic = {}
    w_list = text.split()
    for i in range(len(w_list)-1):
        w = w_list[i].lower()
        w = remove_non_alpha(w)
        w2 = w_list[i+1].lower()
        w2 = remove_non_alpha(w2)
        #print (w,w2)
        ret_dic.setdefault((w,w2),[])
        for x in range(3):
            if (x+i < len(w_list)):
                w3 = w_list[i+x].lower()
                w3 = remove_non_alpha(w3)
                ret_dic[(w,w2)].append(w3)
    return ret_dic


def generate_text(d,start_word,length=50):
    wordlist = []
    next = start_word
    for i in range(length):
        if next not in d:
            break
        wordlist.append(next)
        next = random.choice(d[next])
    return " ".join(wordlist)


#hamlet = bwcff("hamlet.txt")
#psalms = bwcff("psalms.txt")
#sonnets = bwcff("sonnets.txt")
#print(generate_text(sonnets,'fairest'))
#print(build_trigram("sonnets.txt"))


def generate_text(d,start_word,length=10):
    wordlist = []
    next = start_word
    tup_l = list(d.keys())
    used =[]
    for i in range(length):
        if next not in (item[0] for item in tup_l):
            pass
        elif next not in (item[1] for item in tup_l):
            break
        for words in tup_l:
            if (next in words and words not in used):
                hold = words
        wordlist.append(random.choice(d[hold]))
        next = random.choice(d[hold])
    return " ".join(wordlist)

d = build_trigram("sonnets.txt")
print(d)

print(generate_text(d,'fairest', 10))