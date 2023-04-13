#Jednostavni digitron, sa cuvanjem racunskih operacija i naknadnim stampanjem svih.
#Zadavanje liste za kasnije dodavanje i printanje.
resenja = []

#While loop za sprovodjenje ponavljanja samog racunanja, ukoliko ima potrebe.
while True:
    print('Da li zelite da racunate?')
    question = input("d ili n?: ").lower()
    #Pitanja za zapocinjanje i zavrsavanje loopa.
    if question == 'd':
        #Stampanje dostupnih racunskih operacija.
        print("Ponudjene operacije su sabiranje(+), oduzimanje(-), mnozenje(*), deljenje(/).")

        #Unos racunice, stampanje rezultata i dodavanje u listu resenja.
        try:
            unosRacunice = input("Unesite vasu racunicu: ")
            resenje = (str(eval(unosRacunice)))
            print(unosRacunice , '=', resenje)
            resenja.append((unosRacunice, '=', (resenje)))

        except NameError:
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
            print("Hvala sto koristite nas kalkulator.")
            break

    #Sigurnosni else za pogresan unos.
    else:
        print("Pogresan unos, pokusajte ponovo.")
        continue