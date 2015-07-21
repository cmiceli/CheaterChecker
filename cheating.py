import time
import sys
import random

def main():
    if len(sys.argv) < 2:
        print("Usage:\n\tpython3 cheating.py <YOUR_EMAIL>")
        sys.exit(1)

    try:
        assert "@" in sys.argv[1]
    except:
        print("Format the email correctly!")
        sys.exit(2)
    print("Searching databases of known leaked websites...")
    time.sleep(4*(random.randint(2,4)))
    print("Detecting email reuse across many platforms...")
    time.sleep(4*(random.randint(2,4)))
    print("Calculating probabilities of password reuse based on profiles...")
    time.sleep(4*(random.randint(2,4)))
    if random.randint(1,100) % 88 == 0:
        print("You are fine. Your double life has not been leaked onto the internet")
    else:
        print("You have been caught. Give it up while you still have dignity.")
        print("Who knows, if you beg your significant other might forgive you.")

if __name__ == "__main__":
    main()

