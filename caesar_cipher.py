alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cap_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]


def caesar_cipher(msg, shift_num, mode):
    final_text = ""
    
    for char in msg:
        if char in alphabet:
            position = alphabet.index(char)
            if mode == "Decryption" and shift_num > 0:
                shift_num *= -1
            new_position = position + shift_num
            
            final_text += alphabet[new_position]
        elif char in cap_alphabets:
            position = cap_alphabets.index(char)       
            if mode == "Decryption" and shift_num > 0:
                shift_num *= -1
            new_position = position + shift_num
            
            final_text += cap_alphabets[new_position]
        else:
            final_text += char        
    
    return(final_text)
