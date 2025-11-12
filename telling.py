# Funksjon som sjekker om tre verdier er like
def tre_like(a, b, c):
    """
    Returnerer True hvis alle tre verdiene er like,
    ellers False.
    """
    return a == b == c



def double():
    alist = [4, 6, 2, 4, 5, 7, 98, 9999999]
    blist = []
    # keepgoing = True
    # while keepgoing:
    #     gimme = int(input("Gimme a number (ends when number not given) | "))
        # if type(gimme) == int:
        #     alist.append(gimme)
        # else:
        #     keepgoing = False
    
    
    for i in alist:
        doub = i*2
        blist.append(doub)
    
    print(f"original: {alist}")
    print(f"doubled: {blist}")

double()
# sjekkker om de er ulike
def tre_ulik(a, b, c):
    """
    Returnerer True hvis minst én av verdiene er forskjellig,
    ellers False.
    """
    return not (a == b == c)


# Eksemplel
print("Eksempler:")
print("tre_like(5, 5, 5)  =", tre_like(5, 5, 5))   # True
print("tre_like(5, 3, 5)  =", tre_like(5, 3, 5))   # False
print("tre_ulik(5, 5, 5)  =", tre_ulik(5, 5, 5))   # False
print("tre_ulik(5, 3, 5)  =", tre_ulik(5, 3, 5))   # True

def forekomster():
   tekst = input("Skriv noe: ") 
   tegn = input("Hvilket tegn? ")
   antall_tegn = 0

   for i in tekst:
    if i == tegn:
        antall_tegn += 1
        
            
   print(antall_tegn)

forekomster()
