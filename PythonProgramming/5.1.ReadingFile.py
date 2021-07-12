#Program which reads the entire content of the facts.txt file and prints it on the screen
readfile = open("facts.txt")
content = readfile.read()
print("Following was read from the file:", content)
