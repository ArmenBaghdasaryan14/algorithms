class Alphabet():
    unsorted_letters = []
    letter_weight = []

    def get_letters(self, inputArray):
        for word in  inputArray:
            for letter in word:
                try:
                    self.unsorted_letters.index(letter)
                except:
                    self.unsorted_letters.append(letter)
        return self.unsorted_letters


    def get_letter_weight(self, inputArray):
        
        return 0

sampleList = ["baa", "abcd", "abca", "cab", "cad"]

newAlphabet = Alphabet()
newAlphabet.get_letters(sampleList)
print(newAlphabet.unsorted_letters)