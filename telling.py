
def forekomster():
   tekst = input("Skriv noe: ") 
   tegn = input("Hvilket tegn? ")
   antall_tegn = 0

   for i in tekst:
    if i == tegn:
        antall_tegn += 1
        
            
   print(antall_tegn)

forekomster()
