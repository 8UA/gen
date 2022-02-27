# Importing modules
import random
import string
import sys

# User input
lenght = int(input('Strings lenght : '))
lines = int(input('How many lines to generate : '))

def randStr (
        chars = string.ascii_letters + string.digits + string.punctuation, N=lenght):
        return ''.join(random.choice(chars) for _ in range(N))

print ("Generating output... press Ctrl+C to stop.")

# Output strings to file
file_path = 'output.txt'
sys.stdout = open(file_path, "w")

# Generating strings
for x in range(lines):
        print(randStr())
