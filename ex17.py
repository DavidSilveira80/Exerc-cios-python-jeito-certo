from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# poderiamos fazer esses dois com uma linha, como?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

"""
No Terminal execute este script da seguinte forma:
 primeiro crie um arquivo de exemplo:
 echo "Este é um arquivo de teste." > teste_17.txt
 Para verificar seu conteúdo: cat teste_17.txt
 Excute seu script nele: python3 ex17.py teste_17.txt novo_arquivo_17.txt
"""