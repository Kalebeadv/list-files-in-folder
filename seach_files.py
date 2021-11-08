
from os import walk
files = []
path = 'directory'
for (dirpath, dirnames, filenames) in walk(path):
  files.extend(filenames)
  break

print('exemplo')
for numero,arquivo in enumerate(files):
  print(numero + 1, "-",arquivo)
