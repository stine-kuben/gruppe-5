# Funksjon som sjekker om tre verdier er like
def tre_like(a, b, c):
    """
    Returnerer True hvis alle tre verdiene er like,
    ellers False.
    """
    return a == b == c


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

