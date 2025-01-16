import string
from itertools import permutations, product
from datetime import datetime

class PwdCracker():
    def __init__(self, pwd, word_list=None, hash_type=None):
        self.pwd = pwd
        if not self.pwd:
            return "You must enter a password to crack - aborting." 
        self.word_list = word_list
        self.hash_type = hash_type
        self.chars = self.get_characters()
        self.start_time = datetime.now()
        self.iterations = 0

    def get_characters(self):
        chars = string.printable
        characters = []
        for char in chars:
            characters.append(char)
        characters = characters[:95]
        return characters

    def brute_force(self):
        if not self.pwd:
            return("password not entered - try again")

        i = 0
        pwd_guess = []
        while pwd_guess != self.pwd: # This should be a while loop "while pwd_guess != self.pwd"
            pwd_guess = product(self.chars, repeat=i)
            
            for guess in pwd_guess:
                self.iterations += 1
                guess_str = ''.join(str(val) for val in guess)
                time_running = (datetime.now()-self.start_time) 
                time_running = str(time_running).split(".")[0] 
                print(f"[Press 'ctrl+c' to quit] | Trying: {guess_str} | Run time: {time_running} | iterations: {self.iterations:,}", end='\r')
                
                if guess_str == self.pwd:
                    print("\n")
                    return f"Password = {guess_str} | Total run time: {time_running} | total iterations: {self.iterations:,}."
                
            if i >= 6:
                print("\n")
                return "Password is above 6 characters and it would take an estimated average time of 1 hour to crack - You should consider using a wordlist instead.. Bye!"
            i += 1
            
        return "Not Found"
            
