from Caesar import CaesarCipher

class FrequencyAttack:
    def __init__(self):
       self.english_freq = {
            'E': 12.702, 'T': 9.056, 'A': 8.167, 'O': 7.507, 'I': 6.966,
            'N': 6.749, 'S': 6.327, 'H': 6.094, 'R': 5.987, 'D': 4.253,
            'L': 4.025, 'C': 2.782, 'U': 2.758, 'M': 2.406, 'W': 2.360,
            'F': 2.228, 'G': 2.015, 'Y': 1.974, 'P': 1.929, 'B': 1.492,
            'V': 0.978, 'K': 0.772, 'J': 0.153, 'X': 0.150, 'Q': 0.095, 'Z': 0.074
        }
       
       self.cipher=CaesarCipher()
    #    self.alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #    self.alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    
    def frequency_analysis(self,text):
        text_clean=text.replace(" ","").upper()
        letter_count = {}        
        total_letters=0
        
        for char in text_clean:
            if char in self.cipher.uppercase:
                letter_count[char]= letter_count.get(char,0)+1
                total_letters +=1
        
        frequencies={}
        for letter in self.cipher.uppercase:
            if letter in letter_count:
                frequencies[letter]=(letter_count[letter]/total_letters)*100
            else:
                frequencies[letter]=0.0
        
        
        return frequencies, total_letters
       
    def find_key_by_frequency(self, ciphertext):
        
        
         most_frequent=0
         key_candidate=""   
         return key_candidate, most_frequent
       
    def attack_caesar(self, ciphertext):
        print("CipherText: ",ciphertext)
        
        key, most_frequent = self.find_key_by_frequency(ciphertext)
        
        
        plaintext = self.cipher.decipher(ciphertext, key)
        
        print(f"plainText= {plaintext} with key= {key}")
        best_key=""
        best_decipher=""
        return best_key, best_decipher
        
def main():
    ciphertext = "HOHFWURQL HQJLQHHULQJ"
    attack= FrequencyAttack()
    key, plaintext=attack.attack_caesar(ciphertext)

 
 
 
if __name__ == "__main__":
    main()