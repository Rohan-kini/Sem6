def encrypt(plaintext, key):
    ciphertext = ""
    for p, k in zip(plaintext, key):
        # Calculate zero-based indices
        p_index = ord(p) - 65
        k_index = ord(k) - 65
        
        # Perform XOR and adjust result if necessary
        xor_result = p_index ^ k_index
        if xor_result > 25:
            xor_result -= 26
        
        # Convert back to character
        ciphertext += chr(xor_result + 65)
    
    return ciphertext

def decrypt(ciphertext, key):
    decrypted_text = ""
    for c, k in zip(ciphertext, key):
        # Calculate zero-based indices
        c_index = ord(c) - 65
        k_index = ord(k) - 65
        
        # Perform XOR and adjust result if necessary
        xor_result = c_index ^ k_index
        if xor_result > 25:
            xor_result -= 26
        
        # Convert back to character
        decrypted_text += chr(xor_result + 65)
    
    return decrypted_text


def generate_key(plain_text,key):
    if len(plain_text)==len(key):
        return key
    else:
        pad_key=key
        for i in range(len(plain_text)-len(key)):
            pad_key+=key[i%len(key)]
        return pad_key


if __name__=="__main__":
    plain_text="HELLO"
    key="HI"
    pad_key=generate_key(plain_text,key)
    answer=encrypt(plain_text,pad_key)
    print(answer)
    deanswer=decrypt(answer,pad_key)
    print(deanswer)
    
