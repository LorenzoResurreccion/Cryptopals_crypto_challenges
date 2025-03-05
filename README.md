# Cryptopals Crypto Challenges

On the Cryptopals website, they presented various coding challenges pertaining to various topics and ideas within cryptography.\ 
This repository stores my various attempts at creating solutions for these sets of challenges.

## Set 1:
#### Challenge 1: Convert Hex to base64
Given a hex string, converted it into base64 equivalent string\
Implemented functions to split strings into chunks, convert hex to ascii chars, convert num to base64, and hex to base54


#### Challenge 2: Fixed XOR
Given a hex string, XORed it against a single fixed XOR key then converted to ascii chars and printed results\
Implemented a function so conduct the XOR, both key and plaintext were the same length

#### Challenge 3: Single-byte XOR cipher 
Given a hex string, XORed entire string against key of length 1 to decrypt into mos tprobable plaintext\
Implemented functions to perform he single xor as well as scoring the resulting plaintexts\
Essentially functions as encrypytion/decryption of caesar cipher

#### Challenge 4: Detect single-character XOR
Given file containing multiple lines of hex, found the single-byte XOR encrypted cipher text among the lines and printed the plaintext\
Used Previous functions to check each line and saved the single most probable plaintext line from whole file

#### Challenge 5: Implement repeating-key XOR
Given a plaintext, and multiple-chaacter length key, encrypt the plaintext and output the ciphertext\
Implemented functions for performing the encryption and converting integers to hex\
Essentially functions as encryption/decryption of vigenère cipher

#### Challenge 6: Break repeating-key XOR


#### Challenge 7: AES in ECB mode


#### Challenge 8: Detect AES in ECB mode

