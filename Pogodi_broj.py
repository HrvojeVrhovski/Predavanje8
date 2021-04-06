from random import randrange
secret=(randrange(100))
print(secret)
pokusaj=1
print("Pogađanja brojeva")
print("Pogodi broj između 1 i 100 u što manje pokušaja...")

while 1==1:
    guess=int(input("Unesi broj: "))
    if secret > guess:
        print("Moj broj je veći")
        pokusaj=pokusaj + 1
    elif secret < guess:
        print ("Moj broj je manji")
        pokusaj = pokusaj + 1
    else:
        print ("Čestitam, točno, pogodak iz " + str(int(pokusaj)) + ". pokušaja!")
        break
