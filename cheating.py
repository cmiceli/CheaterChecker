import time
import sys
import random

def get_time():
    return 4*(random.randint(2,4))

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
    time.sleep(get_time())
    print("Detecting email reuse across many platforms...")
    time.sleep(get_time())
    print("Calculating probabilities of password reuse based on profiles...")
    time.sleep(get_time())
    print("")
    if random.randint(1,100) % 88 == 0:
        print("\033[92mYou are fine. Your double life has not been leaked onto the internet")
    else:
        print("\033[91mYou have been caught. Give it up while you still have dignity.")
        print("\033[91mWho knows, if you beg your significant other might forgive you.")

if __name__ == "__main__":
    main()

