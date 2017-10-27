#used Quymbee's solution as reference

letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
lt = letters.split()

def rotate_letter(c, r):
    letter = lt.index(c)
    
    if letter < len(lt)-r:
        caesar = letter + r
        return lt[caesar]
    elif letter >= len(lt)-r:
        rot = len(lt) - letter
        caesar = r - rot
        
        return lt[caesar]
    
def encode_string(s, r):
    s2 = s.lower()    
    cipher = []
                
    for i in range(len(s)):
        cipher.append(rotate_letter(s[i], r))
        caesar = "".join(cipher)
        
    return caesar
        
def full_encode(s):
    for i in range(len(lt)):
        print(encode_string(s, i))
    
        
print(rotate_letter("z",7))
print(rotate_letter("o", 4))
print(rotate_letter("j", 2))


word = "child"
print(word)
print(encode_string(word, 7))

full_encode("abcd")
