from functions import split_data

#implementing repeating xor

plaintext = ''
print('Enter plaintext, blank line indicates end of plaintext: ')
while True:
    line = input()
    if line:
        plaintext += line + '\n'
    else:
        break

key = input('Key: ').encode()
plaintext = plaintext.strip().encode()


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

ciphertext = vig_enc(plaintext, key)
print('ciphertext: ',ciphertext)
