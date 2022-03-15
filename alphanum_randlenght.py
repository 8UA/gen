from random import choice, randrange
from string import ascii_letters, digits
from datetime import datetime
from tqdm import tqdm
from time import sleep
import sys

def alphanumRandLen():
        print()
        # User input
        print(" --- RANDOM-LENGHT ver. ---\n")
        lines = int(input('How many lines to generate : '))

        print()
        print ("Generating output... press Ctrl+C to stop.\n")

        # Output strings to file
        stdoutOrigin = sys.stdout 
        sys.stdout = open("output.txt", "w")

        # Counting elapsed time
        start = datetime.now()

        for x in tqdm (range (lines)):
                
                randlen = randrange(8, 16)

                # Generating strings
                def randLenStr (
                chars = ascii_letters + digits, N=randlen):
                        return ''.join(choice(chars) for _ in range(N))
                        
                print(randLenStr())

        # Stop counting
        end = datetime.now()

        sleep(0.5)

        # Close file and revert back to code
        sys.stdout.close()
        sys.stdout = stdoutOrigin

        print("Done! \n")
        print("[ Time elapsed ]")
        print(end-start)

if __name__ == "__main__":
        alphanumRandLen()