# #  For il primo loop che andiamo a vedere

# Frutto1 = input("inserisci il tuo primo frutto")
# #Frutto2 = input("inserisci il tuo secondo frutto")

# def stampa_frutto (x):
#     if x == "banana":
#      print(x)
#     else:
#      print("frutto non presente") 

# def frutto_ce(x):
#     print("frutto presente")

# def frutto_nonce(x):
#     print("frutto non presente")

# fruits = ["apple","banana","mela","mango"]
# fruits.__len__ 

# for x in fruits:
#    if x == Frutto1:
#        frutto_ce(x)
#        break
#    if x != Frutto1:
#        frutto_nonce(x)


#  Iniziamo a parlare ora di LOOP e/o ITERATORI
#   Sono uno degli elementi più complessi da inserire senza trouble shotting
#   Un motivo di persistere una ending condition
#  While  ripete ed Esegue un insieme di condizioni purchè la condizione sia vera


thismca = {
  'Nome' : "Manuel",
  'Cognome' : "Rossi",
  'years': 1980
}

i = input( "che operazione vuoi fare?  aggiungi / stampa / cancella/ esci " )
i2 = 0
while i2 <= 1:
 #While i != NULL:
  while i != "esci":
 
   # Menu uno
    if i == "stampa":
       print(thismca)
       i = input( "che operazione vuoi fare?  aggiungi / stampa / cancella / esci " )

    if i == "aggiungi":
       thismca["Cognome"] = input( "Quale cognome vuoi inserire?" )
       i = input( "che operazione vuoi fare?  aggiungi / stampa / cancella / esci " )

    if i == "cancella":
       del thismca["Nome"]
       print('Elemento cancellato') 
       i2 +=1
       break 

    if i == "esci":
      break
  else:
   i = input( "sei sicuro? si/no " )
   if i == "si":
     print("Ciao, alla prossima") 
     i2 +=1
     break
    
   if i == "no":  
     i = input( "che operazione vuoi fare?  aggiungi / stampa / cancella / esci " )


print("grazie mille")
 
