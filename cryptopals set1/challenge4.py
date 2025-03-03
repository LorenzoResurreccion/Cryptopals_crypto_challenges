# detect single character XOR
#filename: cryptopals_s1_c4.txt
filename = input('Name of file: ')

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
        



data = []
# read lines
with open(filename,'r') as file:
    # read lines
    for line in file:
        data.append(bytes.fromhex(line))




# track best metrics
max_score = 0 
best = ''
key  = 0


#calc most likely plaaintext of line, save best overall
for line in data:
    for num in range(255):
        res = single_xor(line, num)
        
        # use character frequencies to save str
        score = score_Eng(res)
        if score > 0:
            
            if res == b'Now that the party is jumping':
                print('found')
        if score > max_score:
            max_score= score
            best = res
            key = num


# display results
print('key:', key, max_score)
print('plaintext:', best)

        
