import string

'''implemented in challenge 1'''
#hex alphebet for quick conversion from char to int
hex_to_num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,'6':6, '7':7, '8':8, 
       '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

# split hex into chunks
def split_data(data, size):
    curr = []
    res = []
    # split into pairs to be converted
    for c in data:
        curr.append(c)
        if len(curr) == size:
            res.append(curr[:])
            curr = []
    if curr:
        res.append(curr[:])
    return res

# convert hex to chars
def hex_to_char(data):
    data = split_data(data, 2)
    converted = []
    for c1, c2 in data:
        c1= hex_to_num[c1]
        c2 = hex_to_num[c2]
        byte = c1 <<4 | c2
        converted.append(byte)

    return bytes(converted)

# convert  num to b64 char
def num_to_base64(num):
    if 0 <= num <= 25:
        return string.ascii_uppercase[num]
    elif 26 <= num <= 51:
        return string.ascii_lowercase[num - 26]
    elif 52 <= num <= 61:
        return string.digits[num - 52]
    elif num == 62:
        return '+'
    elif num == 63:
        return '/'
    else:
        return None 


# converts hext to b64 chars
def hex_to_b64(data):
    # split into groups of 3
    data = split_data(data, 3)
    converted = ''



'''implemnted in challenge 3'''
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
        if chr(char) not in string.printable:
           return 0
    
        #check common chars: more common == more pts
        amt = common.find(char)
        if amt != -1:
            score += amt
  
    return score

'''implemented in challenge 5'''
num_to_hex = {0:'0',  1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7',
            8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}


#fxn for turning intger into hex
def int_to_hex(num):
    chr1 = num >>4
    chr2 = num & 15
    return num_to_hex[chr1] + num_to_hex[chr2]


#fxn for implementing multi-char key encryption
def vig_enc(data, key):
    n = len(key)
    key_idx = 0
    res = ''
    for byte in data:
        num = byte ^ key[key_idx]
        hex_num = int_to_hex(num)
        res += hex_num
        key_idx = (key_idx + 1) % n
    return res

        
