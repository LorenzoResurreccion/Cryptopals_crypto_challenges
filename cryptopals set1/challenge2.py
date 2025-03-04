#challenge 2: Fixed XOR
hex_str = input('Enter hex string: ')

raw = bytes.fromhex(hex_str)
fixed = bytes.fromhex('686974207468652062756c6c277320657965')

def single_xor(s, key):
    res = [byte ^ key for byte in s]
    return bytes(res)

xored = single_xor(raw, fixed)
print('xored and hex decoded string:', xored.decode('utf-8'))