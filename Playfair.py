
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
        
        
        
        
def main():
    key = "PASSWORD"


if __name__ == "__main__":
    main()