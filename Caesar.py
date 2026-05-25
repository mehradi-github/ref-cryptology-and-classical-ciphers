class CaesarCipher:
    def __init__(self):
        self.uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.lowercase = 'abcdefghijklmnopqrstuvwxyz'
        
    def encipher(self,plaintext,key):    
        ciphertext=[]
        for char in plaintext:
            if char in self.uppercase:
                origin_index=self.uppercase.index(char)
                new_index= (origin_index+key) % 26
                ciphertext.append(self.uppercase[new_index])
            elif char in self.lowercase:
                origin_index=self.lowercase.index(char)
                new_index= (origin_index+key) % 26
                ciphertext.append(self.lowercase[new_index])
            else:    
                ciphertext.append(char)
        return ''.join(ciphertext)

def main():
    cipher=CaesarCipher()
    
    while True:
        print("1. Encipher")
        
        choise=input("Your choice: ")
        
        if choise=='1':
            plaintext= input("PlainText (english letters): ")
            key=int(input("Key (int): "))
            ciphertext= cipher.encipher(plaintext,key)
            print(f"Ciphertext:{ciphertext}")
        elif choise=='4':
            print("Exiting program.")
            break
        else:
            print("Invalid input. please enter 1, 2, 3 or 4.")  
    
if __name__ == "__main__":    
    main()
