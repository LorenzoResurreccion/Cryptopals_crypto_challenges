#single byte XOR cipher
hex_str = input('Enter hex string: ')
base_str = bytes.fromhex(hex_str)


# stores most common chars in reversed order: #etaoin shrdlu
common = b"etaoin shrdlu"[::-1]


#xor full string against  single char
def single_xor(s, key):
    res = [byte ^ key for byte in s]
    return bytes(res)

#calc english score 
def score_Eng(s):
    score = 0
    s = s.lower()
    
    #iteate through chars of string
    for char in s:
        if not chr(char).isprintable():
           return 0
    
        #check common chars: more common == more pts
        amt = common.find(char)
        if amt != -1:
            score += amt
  
    return score
        
# track most likely plaintext
max_score = 0 
best = ''
key  = 0

#try all possible chars
for num in range(255):
    res = single_xor(base_str, num)
    # use character frequencies to save str
    score = score_Eng(res)
    if score > max_score:
        max_score= score
        best = res
        key = num

# print results
print('key:', key)
print('decoded string:',  best.decode('utf-8'))
