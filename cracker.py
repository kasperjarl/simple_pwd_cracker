import string

class PwdCracker():
    def __init__(self, pwd="p", word_list=None, hash_type=None):
        self.pwd = pwd
        self.word_list = word_list
        self.hash_type = hash_type
        self.all_ascii_chars = self.get_characters()

    def get_characters(self):
        all_ascii_chars = string.printable
        characters = []
        for char in all_ascii_chars:
            characters.append(char)
        characters = characters[:95]
        return characters
        
        

    def brute_force(self):
        if not self.pwd:
            return("password not entered - try again")

        pwd_guess = ["a"] # initiate possible characters to be 1

        for i in self.all_ascii_chars:
            pwd_guess[0] = i
            if str(pwd_guess) == self.pwd:
                res = f"Cracked the password: {pwd_guess}"
                return res
            
        return "Not Found"
            



test = PwdCracker()
print(test.brute_force())
