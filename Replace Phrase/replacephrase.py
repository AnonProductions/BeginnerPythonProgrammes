import sys
title = input("What is the name of your notebook? ") + ".txt"

f = open(title, "r")
try:
    f.read()
    content = f.read()
    print(content)
    f.close()
except:
    print(f"No notebook with the name {title} exists")
    sys.exit()

replace_word = input("Which phrase do you want to replace in the note? ")
new_word = input("Which phrase do you want to replace it with? ")

content = content.replace(replace_word, new_word)

f = open(title, 'w')
f.write(content)
f.close()