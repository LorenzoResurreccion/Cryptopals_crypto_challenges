from functions import hex_to_char, score_Eng, single_xor

# detect single character XOR
#filename: cryptopals_s1_c4.txt
filename = input('Name of file: ')

data = []
# read lines
with open(filename,'r') as file:
    # read lines
    for line in file:
        line = hex_to_char(line.strip())
        data.append(line)

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

        if score > max_score:
            max_score= score
            best = res
            key = num

# display results
print('plaintext:', best)

        
