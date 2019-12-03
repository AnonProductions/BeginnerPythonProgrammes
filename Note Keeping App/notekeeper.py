title = input("What is the name of your notebook?") + ".txt"
text = input("What do you want to add/write to the notebook?")

f = open(title, 'a')

f.write(text)
f.close()