def string_times(str, n): #string_times('Hit', 3)
  result = ""
  for i in range(n):  
    result = result + str  
  return(result)

def front_times(str, n): #front_times('Chocolate', 3)
    front_len = 3
    if front_len > len(str):
        front_len = len(str)
    front = str[:front_len]
  
    result = ""
    for i in range(n):
        result = result + front
    return result

def string_bits(str): #string_bits('Preach')
    result=""
    for i in range(len(str)):
        if i % 2 == 0:
            result=result + str[i]
    return result

def lone_sum(a, b, c): #lone_sum(3, 5, 3)

  sum = 0
  sum += a if a not in [b,c] else 0
  sum += b if b not in [a,c] else 0
  sum += c if c not in [a,b] else 0
  return sum

def string_splosion(str): #Problem 5 string_splosion('Crazy')
  result = ""
  
  for i in range(len(str)):
    result = result + str[:i+1]
  return result


def cigar_party(cigars, is_weekend): #cigar_party(50, True)
  if is_weekend:
    if cigars >= 40:
      return True
  elif cigars >= 40 and cigars <= 60:
      return True
  else:
    return False

def caught_speeding(speed, is_birthday): #caught_speeding(60, False)
  if(is_birthday):
    if(speed <= 85):
      if(speed<= 65):
        return 0
      elif(speed>=66):
        return 1
    else:
      return 2
  else:    
    if(speed <= 80):
      if(speed<= 60):
        return 0
      elif(speed>=61):
        return 1
    else:
      return 2
print(string_times('Hit',3))
print(front_times('Chocolate',3))
print(string_bits('Preach'))
print(lone_sum(1, 3, 3))
print(string_splosion('Candy'))
print(cigar_party(60, False))
print(caught_speeding(85, True))
      