import random
import time
liczba1 = 0
liczba2 = 0
prawid_odp = 0
odp = 0
prawid_odp_il = 0
zle_odp_il = 0
pytanienr = 0


def powitanie():
    print ("==========NAUKA TABLICZKI MNOŻENIA DO 100==========")
    time.sleep(0.1)
    print ()
    time.sleep(0.1)
    print ()
    time.sleep(0.1)
    pytanie()

def pytanie():
    liczba1 = random.randint(1,10)
    liczba2 = random.randint(1,10)
    prawid_odp = liczba1 * liczba2
    pytanienr = pytanienr + 1
    print ("Pytanie nr.%s" %pytanienr)
    print (liczba1, " * ", liczba2, " = ", end=" ")
    odp = int(input())
    if odp == prawid_odp:
        print ("Brawo, podałeś/aś dobry wynik!")
        time.sleep(0.1)
        print("Liczba prawidłowych wyników to: %s"%prawid_odp_il)
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        print()
        time.sleep(0.1)
        pytanieplus()
        pytanie()

powitanie()





