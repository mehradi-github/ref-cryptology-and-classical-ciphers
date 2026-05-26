import math

class ColumnarTranspositionCipher:
    def __init__(self, key):
        self.key = key
        self.num_cols = 5
        self.padding = ['a', 'b', 'c', 'd', 'e']
        
    def encipher(self, plaintext):
        plaintext = plaintext.replace(" ", "").lower()
        num_rows = math.ceil(len(plaintext) / self.num_cols)
        
        matrix = [['' for _ in range(self.num_cols)] for _ in range(num_rows)]
        index = 0
        pad_index = 0
        for r in range(num_rows):
            for c in range(self.num_cols):
                if index < len(plaintext):
                    matrix[r][c] = plaintext[index]
                    index += 1
                else:
                    matrix[r][c] = self.padding[pad_index % self.num_cols]
                    pad_index += 1
        
        
        order = [col for _, col in sorted([(self.key[c], c) for c in range(self.num_cols)])]
        
        return ''.join(matrix[r][c] for c in order for r in range(num_rows))
        
    def decipher(self, ciphertext):
        ciphertext = ciphertext.replace(" ", "").lower()
        num_rows = math.ceil(len(ciphertext) / self.num_cols)
        
        order = [col for _, col in sorted([(self.key[c], c) for c in range(self.num_cols)])]
        
        col_len = [num_rows] * self.num_cols
        for i in range(self.num_cols * num_rows - len(ciphertext)):
            col_len[order[-(i+1)]] -= 1
        
        matrix = [['' for _ in range(self.num_cols)] for _ in range(num_rows)]
        index = 0
        for c in order:
            for r in range(col_len[c]):
                matrix[r][c] = ciphertext[index]
                index += 1
        
        result = ''
        for r in range(num_rows):
            for c in range(self.num_cols):
                if matrix[r][c]:
                    result += matrix[r][c]
        
        while result and result[-1] in self.padding:
            result = result[:-1]
        
        return result
        
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