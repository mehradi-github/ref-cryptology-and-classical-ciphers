
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
    
    def decipher(self, ciphertext):
        fence = [[] for _ in range(self.rails)]        
        rail = 0
        direction = 1
        
        positions = []
        for i in range(len(ciphertext)):
            positions.append(rail)            
            if rail == 0:
                direction = 1
            elif rail == self.rails - 1:
                direction = -1            
            rail += direction
        
        rail_counts = [0] * self.rails
        for pos in positions:
            rail_counts[pos] += 1
        
        index = 0
        for i in range(self.rails):
            for j in range(rail_counts[i]):
                fence[i].append(ciphertext[index])
                index += 1
        
        plaintext = []
        rail = 0
        direction = 1
        pointers = [0] * self.rails
        
        for i in range(len(ciphertext)):
            plaintext.append(fence[rail][pointers[rail]])
            pointers[rail] += 1
            
            if rail == 0:
                direction = 1
            elif rail == self.rails - 1:
                direction = -1
            
            rail += direction
        
        return ''.join(plaintext)
    
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