#Jednostavni digitron, sa cuvanjem racunskih operacija i naknadnim stampanjem svih.
#Zadavanje liste za kasnije dodavanje i printanje.
resenja = []

#While loop za sprovodjenje ponavljanja samog racunanja, ukoliko ima potrebe.
while True:
    print('Da li zelite da racunate?')
    question = input("d ili n?: ").lower()
    #Pitanja za zapocinjanje i zavrsavanje loopa.
    if question == 'd':
        #Uzimanje brojeva za input od korisnika.
        a = int(input("Unesite prvi broj: "))
        b = int(input("Unesite drugi broj: "))
        try:
            #Stampanje dostupnih racunskih operacija.
            print("Ponudjene operacije su sabiranje(+), oduzimanje(-), mnozenje(*), deljenje(/).")
            operacija = input("Izaberite racunsku operaciju: ")
            #If i elif statmenti za izvrsavanje operacija.
            if operacija == '+':
                print("Rezultat zbira vasih brojeva je:")
                print(a+b)
                resenja.append("{} + {} = {}".format(a,b, a+b).split(' '))
                    
            elif operacija == '-':
                print("Rezultat oduzimanja vasih brojeva je:")
                print(a - b)
                resenja.append("{} - {} = {}".format(a,b, a-b).split(' '))
                    
            elif operacija == '*':
                print("Rezultat mnozenja vasih brojeva je:")
                print(a*b)
                resenja.append("{} * {} = {}".format(a,b, a*b).split(' '))
                        
            elif operacija == '/':
                print("Rezultat deljenja vasih brojeva je:")
                print(a/b)
                resenja.append("{} / {} = {}".format(a,b, a/b).split(' '))
                    
            else:
                print("Izabrali ste pogresnu operaciju.")
                continue
        except ValueError:
            print("Vas unos nije broj.")
            continue

    #Zavrsavanje while loopa sa printom liste.
    elif question == 'n':
        if len(resenja) > 0:
            print("Vasa prethodno uneta racunanja su: ")
            for i in (resenja):
                print(' '.join(i))
            break
        else:
            print("Nema prethodno unetih racunanja.")
            print("Hvala sto koristite nas digitron.")
            break

    #Sigurnosni else za pogresan unos.
    else:
        print("Pogresan unos, pokusajte ponovo.")
        continue