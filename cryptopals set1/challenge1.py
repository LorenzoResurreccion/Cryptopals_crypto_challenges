import base64
import string


#hex alphebet for quick conversion from char to int
hex = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,'6':6, '7':7, '8':8, 
       '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}


#challenge 1: hex to base64
hex_str = input('Enter hex string: ')

# split hex into chunks
def split_hex(data, size):
    n = int(len(data)/size)
    res = []
    # split into pairs to be converted
    for i in range(n):
        idx1 = size*i
        idx2 = idx1+size
        res.append(data[idx1:idx2])
    return res

# convert hex to chars
def hex_to_char(data):
    data = split_hex(data, 2)
    converted = ''
    for pair in data:
        bin1 = bin(hex[pair[0]])[2:].zfill(4)
        bin2 = bin(hex[pair[1]])[2:].zfill(4)
        byte = str(bin1) + str(bin2)
        num = int(byte,  2)
        converted+= chr(num)

    return converted

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
    data = split_hex(data, 3)
    converted = ''

    # convert 3 chars into binary: 2 b64 chars
    for trio in data:
        bin1 = bin(hex[trio[0]])[2:].zfill(4)
        bin2 = bin(hex[trio[1]])[2:].zfill(4)
        bin3 = bin(hex[trio[2]])[2:].zfill(4)
        full_bin= str(bin1) + str(bin2) + str(bin3)
        num1 = int(full_bin[:6],  2) # numval of char1
        num2 = int(full_bin[6:], 2)# num val of char 2
        
        converted+= num_to_base64(num1) + num_to_base64(num2)

    return converted
result = hex_to_b64(hex_str)
print('result:', result)