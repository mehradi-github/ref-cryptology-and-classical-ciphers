
class RailFenceCipher:
    def __init__(self, key):
        pass

def main():
    cipher = RailFenceCipher(4)
    
    plaintext = "Informationtechnologyx"    
    ciphertext = cipher.encipher(plaintext)
    
    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    
    print("-" * 10)
    ciphertext = "hvmkayatoabfehabratdad"    
    plaintext = cipher.decipher(ciphertext)
    
    print(f"Ciphertext: {ciphertext}")
    print(f"Plaintext:  {plaintext}")


if __name__ == "__main__":
    main()