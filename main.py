from cracker import PwdCracker

def main():
    password = input("Enter password to crack: ")
    w = PwdCracker(pwd=password)
    w.brute_force()

if __name__ == "__main__":
    main()