import json
import Classtkinter
from tkinter import messagebox

#"C:\\Progetti\\Progetti\\04.Varie\\IFS\\CorsoPython\\ProvaFile.txt"

def caricaArray(indice) :
  i = 0
  while  i <= int(indice):
      elemento = input('Inserisci il nuovo elemento :' )
      lista.append(elemento)
      i+=1
  return lista

def CreaFile(array, Path):
  for value in array:
      f = open(Path, "a")
      f.write(value + "\n")
      f.close()

def LeggiCastaFile():
  f = open(Path, "r") 
  testo = f.read()
  #return print(json.loads(json.dumps(testo)))
  return json.loads(json.dumps(testo))


#*******************************************************************

lista = []
indice  = input("Inserisci il numero di elementi da gestire nella tua lista: ")
lblFile = input("Inserisci il nome del file che vuoi creare: ")
Path = Classtkinter.search_for_file_path().replace("/","\\") + "\\" + lblFile

x = caricaArray(indice)
x = CreaFile(x, Path)
x = LeggiCastaFile()

messagebox.showinfo("Contenuto del file creato", x)
