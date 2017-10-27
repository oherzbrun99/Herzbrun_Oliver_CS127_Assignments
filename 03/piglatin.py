def piglatinify():
    words = "The cat in my hat sat on the mat and shat an innumerable amount of fat"
    piglatinify = words.split()
    for word in words:
        if words[0] == "a e i o u":
            print(words + "ay")
        else:
            word[0] = dil
            words = words[1:]
            print(words + dil + "ay")
            

        

         
