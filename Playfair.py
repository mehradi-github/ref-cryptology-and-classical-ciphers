
class PlayfairCipher:
    def __init__(self, key):
        self.alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' 
        self.key = key.upper()
        self.matrix = []
        self.create_matrix()
        
        
    def create_matrix(self):
        combined = []
        
        for char in self.key:
            if char not in combined and char != 'J':
                combined.append(char)
            elif char == 'J' and 'I' not in combined:
                combined.append('I')     
       
        for char in self.alphabet:
            if char not in combined:
                combined.append(char)
        
        self.matrix = [combined[i:i+5] for i in range(0, 25, 5)]
        
    
    def prepare_text(self, text):
        text = text.upper()
        text = text.replace('J', 'I')
        
        text = ''.join([c for c in text if c.isalpha()])
        
        pairs = []
        i = 0
        while i < len(text):
            a = text[i]
            if i + 1 < len(text):
                b = text[i + 1]
                if a == b:
                    pairs.append(a + 'X')
                    i += 1
                else:
                    pairs.append(a + b)
                    i += 2
            else:
                pairs.append(a + 'X')
                i += 1
        
        return pairs
    
    def find_position(self, char):
        if char == 'J':
            char = 'I'
        
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return i, j
        return None
    
    def encrypt_pair(self, a, b):        
        row1, col1 = self.find_position(a)
        row2, col2 = self.find_position(b)
        
        if row1 == row2:
            return (self.matrix[row1][(col1 + 1) % 5] + self.matrix[row2][(col2 + 1) % 5])        
        elif col1 == col2:
            return (self.matrix[(row1 + 1) % 5][col1] + self.matrix[(row2 + 1) % 5][col2])        
        else:
            return (self.matrix[row1][col2] + self.matrix[row2][col1])
               
    def encipher(self, plaintext):
        pairs = self.prepare_text(plaintext)
        ciphertext = []
        
        for pair in pairs:
            encrypted_pair = self.encrypt_pair(pair[0], pair[1])
            ciphertext.append(encrypted_pair)
        
        return ''.join(ciphertext)    
        
        
def main():
    key = "PASSWORD"


if __name__ == "__main__":
    main()