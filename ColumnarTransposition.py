import math

class ColumnarTranspositionCipher:
    def __init__(self, key):
        self.key = key
        self.num_cols = len(key)
        
    def encipher(self, plaintext):
        plaintext = plaintext.replace(" ", "").lower()
        num_rows = math.ceil(len(plaintext) / self.num_cols)
        
        matrix = [['' for _ in range(self.num_cols)] for _ in range(num_rows)]
        index = 0
        for r in range(num_rows):
            for c in range(self.num_cols):
                if index < len(plaintext):
                    matrix[r][c] = plaintext[index]
                    index += 1
                else:
                    matrix[r][c] = 'x'
        
        key_order = [(self.key[c], c) for c in range(self.num_cols)]
        key_order.sort(key=lambda x: x[0])
        reading_order = [c for _, c in key_order]
        
        result = []
        for c in reading_order:
            for r in range(num_rows):
                result.append(matrix[r][c])
        
        return ''.join(result)
        
            
def main():
    cipher = ColumnarTranspositionCipher([5, 3, 4, 2, 1])
    
    plaintext = "ramznegarilezzatbakhshast"    
    ciphertext = cipher.encipher(plaintext)
    
    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    
    # print("-" * 10)
    
    # cipher = ColumnarTranspositionCipher([4, 5, 3, 1, 2])
    # ciphertext = "eehibleoncmtmeamlmsiaaasm"    
    # plaintext = cipher.decipher(ciphertext)
    
    # print(f"Ciphertext: {ciphertext}")
    # print(f"Plaintext:  {plaintext}")


if __name__ == "__main__":
    main()