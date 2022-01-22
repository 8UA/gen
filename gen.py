import random
import string
import sys

print("Generating output... press Ctrl+C to stop.")

#output file
file_path = 'output.txt'
sys.stdout = open(file_path, "w")

#infinitely generates random strings
while True:
    def randStr(chars = '[@_!#$£%^&*()<>?/\|}{~:]' + string.ascii_letters + string.digits, N=16):
        return ''.join(random.choice(chars) for _ in range(N))
    print(randStr())
