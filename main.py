
def encryption(plaintext):
    eventext = []
    oddtext = []
    for i in range(0, len(plaintext)):
        if i % 2 == 0:
            eventext.append(plaintext[i])
        else:
            oddtext.append(plaintext[i])
    print("Even Text : ", eventext)
    print("Odd Text : ", oddtext)
    ciphertext = eventext + oddtext
    return ciphertext

def decryption(ciphertext):
    if len(ciphertext) % 2 != 0:
        ciphertext.append("")
    length = int(len(ciphertext)//2)
    evenletters = ciphertext[:length]
    oddletters = ciphertext[length:]

    decryptedtext = []
    for x in range(length):
        decryptedtext.append(evenletters[x])
        decryptedtext.append(oddletters[x])
    return decryptedtext


plaintext = input("Enter The Plain Text : ")
cipherText = encryption(plaintext)
print("Encryption : ", cipherText)
DecMethod = decryption(cipherText)
print("Decryption : ", DecMethod)
