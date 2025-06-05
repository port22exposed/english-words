import re
import sys

output = open("roblox_name_words.txt", "w")

words = open(sys.argv[1])
word_list = words.readlines()

def is_alphanumeric_underscore(s):
    return bool(re.match(r'^\w+$', s))

for i, word in enumerate(word_list):
    word = word.strip()
    if len(word) > 3 and len(word) <= 20 and is_alphanumeric_underscore(word):
        if i < len(word_list) - 1:
            output.write(f"{word}\n")
        else:
            output.write(word)

output.close()