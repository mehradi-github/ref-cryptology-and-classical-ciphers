
class RailFenceCipher:
    def __init__(self, rails):
        self.rails = rails

    def encipher(self, plaintext):
        plaintext = plaintext.replace(" ", "")
        
        fence = [[] for _ in range(self.rails)]
        
        rail = 0
        direction = 1  
        
        for char in plaintext:
            fence[rail].append(char)            
            if rail == 0:
                direction = 1
            elif rail == self.rails - 1:
                direction = -1
            
            rail += direction
        
        ciphertext = ''.join([''.join(rail) for rail in fence])
        
        return ciphertext
    
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