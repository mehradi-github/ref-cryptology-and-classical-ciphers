class ColumnarTranspositionCipher:
    def __init__(self, key):
        self.key = key
        self.num_cols = len(key)
            
def main():
    cipher = ColumnarTranspositionCipher([5, 3, 4, 2, 1])
    
    plaintext = "ramznegarilezzatbakhshast"    
    ciphertext = cipher.encipher(plaintext)
    
    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    
    print("-" * 10)
    
    cipher = ColumnarTranspositionCipher([4, 5, 3, 1, 2])
    ciphertext = "eehibleoncmtmeamlmsiaaasm"    
    plaintext = cipher.decipher(ciphertext)
    
    print(f"Ciphertext: {ciphertext}")
    print(f"Plaintext:  {plaintext}")


if __name__ == "__main__":
    main()