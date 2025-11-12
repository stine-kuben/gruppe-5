


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