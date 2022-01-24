import random
import string
import sys

#user input
lenght = int(input('Strings lenght : '))
lines = int(input('How many lines to generate : '))

def randStr (chars = '[@_!#$£%^&*()<>?/\|}{~:]' + string.ascii_letters + string.digits, N=lenght):
        return ''.join(random.choice(chars) for _ in range(N))

print ("Generating output... press Ctrl+C to stop.")

#output strings to file
file_path = 'output.txt'
sys.stdout = open(file_path, "w")

#generating strings
for x in range(lines):
        print(randStr())