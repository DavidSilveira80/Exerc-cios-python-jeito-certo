from sys import argv
# Execute o programa no terminal do seguinte modo: python3 ex15.py ex15_sample.txt
# Digite no prompt:  > ex15_sample.txt 
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
