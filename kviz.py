import random

#Poruka dobrodoslice.
print("Dobro dosli u kviz Ko ne zna, neka nauci!")

pitanjaGeografija = {

    'pitanje0' : "Najrasprostranjeniji tip zemljišta u Srbiji je?",
    'pitanje1' : "Kakvo je Palićko jezero po postanku? ",
    'pitanje2' : "Koji je glavni grad Holandije? ",
    'pitanje3' : "Koji moreuz povezuje Sredozemno more i Atlantski okean?",
    'pitanje4' : "Koji je najveći kontinent na svetu?",
    'pitanje5' : "Koji je najveći okean na Zemlji? ",
    'pitanje6' : "Kako se zove najvisi vrh Srbije? ",
    'pitanje7' : "Kako se zove topla struja u severnom Atlantiku? ",
    'pitanje8' : "Koja zemlja je najveci proizvodjac secerne trske? ",
    'pitanje9' : "Gde se pojavilo klinasto pismo?"

}

pitanjaIstorija = {

    'pitanje0' : "Kako su glasila imena trojice sinova Stefana Nemanje?",
    'pitanje1' : "Srpski vazal Lazar Hrebeljanovic je nosio titulu?",
    'pitanje2' : "Manastir Milesevu je podigao?",
    'pitanje3' : "U kom mestu je Karađorđe izabran za vođu Prvog srpskog ustanka?",
    'pitanje4' : "Koje godine je Kristofor Kolumbo otkrio Ameriku? ",
    'pitanje5' : "U kojoj današnjoj državi je 1914. godine ubijen nadvojvoda Franc Ferdinand?",
    'pitanje6' : "Koje godine dolazi do poslednje smene dinastija Obrenović i Karađorđević na čelu Srbije?",
    'pitanje7' : "Vreme trajanja drugog svetskog rata? (napisati godine).",
    'pitanje8' : "Koji italijanski grad je nastradao nakon erupcije Vezuva 79. godine?",
    'pitanje9' : "Koje carstvo je utemeljio Džingis-kan?"
    
}

pitanjaOpstaKultura= {

    'pitanje0' : "Ko se nalazi na novcanici od 500 dinara? ",
    'pitanje1' : "Kako se zove himna Republike Srbije? ",
    'pitanje2' : "Koji padez u srpskom jeziku postavlja pitanje koga? ",
    'pitanje3' : "Koja je priblizna vrednost broja Pi? ",
    'pitanje4' : "Najpopularnija drustvena mreza za povezivanje profesionalaca je? ",
    'pitanje5' : "Rec avlija je rec kog porekla?",
    'pitanje6' : "Film “Kum” rezirao je?",
    'pitanje7' : "Cime se bavi kaligrafija? ",
    'pitanje8' : "Ptica feniks je symbol cega? ",
    'pitanje9' : "Ko je izumeo Penicilin? "
    
}

pitanjaSport = {

    'pitanje0' : "U kom sportu se proslavio Diego Maradona? ",
    'pitanje1' : "Koji teniser drzi record u najvise nedelja provedenih na vrhu ATP liste? ",
    'pitanje2' : "Kvoterbek je pozicija u kom sportu?",
    'pitanje3' : "Bruklin netsi su tim u kom sportu? ",
    'pitanje4' : "Koje godine je zvezda osvojila Kup sampiona? ",
    'pitanje5' : "Ko je bio najmladji borac u boksu koji je ikada osvojio svetsko prvenstvo u teskoj kategoriji?",
    'pitanje6' : "Gde je sediste svetske profesionalne bilijar I snuker asocijacije? ",
    'pitanje7' : "Kako se zove stadion fudbalskog kluba Partizan? ",
    'pitanje8' : "Ko je proglasen za mvp-a (najkorisnijeg igraca) NBA lige u 2021 godini? ",
    'pitanje9' : "U kom sportu se koristi Arlberg tehnika? "
    
}

odgovoriGeografija = {

    'odgovor0' : ['crnica','cernozem','černozem','чернозем','црница'],
    'odgovor1' : ['природно','еолско','prirodno','eolsko','prirodno eolsko','природно еолско'],
    'odgovor2' : ['амстердам','amsterdam'],
    'odgovor3' : ['гибралтар','гибралтарски мореуз','gibraltar','gibraltarski moreuz'],
    'odgovor4' : ['azija','азија'],
    'odgovor5' : ['tihi okean','тиги океан','тихи','tihi'],
    'odgovor6' : ['djeravica','ђеравица'],
    'odgovor7' : ['голфска струја','голфска','golfska struja','golfska'],
    'odgovor8' : ['brazil','бразил'],
    'odgovor9' : ['месопотамија','mesopotamija','mesopotamiji','u mesopotamiji','месопотамији','у месопотамији']
    
}

odgovoriIstorija = {

    'odgovor0' : ['vukan stefan rastko','vukan rastko stefan','stefan rastko vukan','rastko vukan stefan','rastko stefan vukan',
                  'вукан стефан растко','вукан растко стефан','стефан растко вукан','растко вукан стефан','растко стефан вукан'],
    'odgovor1' : ['kneza','кнеза','titulu kneza','титулу кнеза'],
    'odgovor2' : ['kralj vladislav','краљ владислав'],
    'odgovor3' : ['orascu','orašcu','орашцу','u orascu','u orašcu','у орашцу'],
    'odgovor4' : ['1492'],
    'odgovor5' : ['u bosni','bosni i hercegovini','bosni','у босни','босни','босни и херцеговини'],
    'odgovor6' : ['1903'],
    'odgovor7' : ['1939-1945','1939 - 1945','1939 1945',],
    'odgovor8' : ['pompeja', 'помпеја'],
    'odgovor9' : ['mongolsko','mongolsko carstvo','монголско','монголско царство']
    
}

odgovoriOpstaKultura = {

    'odgovor0' : ['jovan cvijic','jovan cvijić','јован цвијић'],
    'odgovor1' : ['boze pravde','bože pravde','боже правде'],
    'odgovor2' : ['genitiv','генитив'],
    'odgovor3' : ['3.14','3,14'],
    'odgovor4' : ['linked in','linkedin','линкед ин','линкедин'],
    'odgovor5' : ['turcizam','turskog','турцизам','турског'],
    'odgovor6' : ['frencis ford kopola','frencis kopola','frencis ford','френцис форд копола','френцис копола','френцис форд'],
    'odgovor7' : ['lepim pisanjem','лепим писањем'],
    'odgovor8' : ['besmrtnosti','бесмртности'],
    'odgovor9' : ['aleksandar fleming', 'александар флеминг']
    
}

odgovoriSport = {

    'odgovor0' : ['fudbalu','fudbal','фудбалу','фудбал'],
    'odgovor1' : ['novak djokovic','novak đoković','новак ђоковић'],
    'odgovor2' : ['ragbi','americki fudbal','američki fudbal','рагби','амерички фудбал','u ragbiju','у рагбију','у америчком фудбалу','u americkom fudbalu','u američkom fudbalu'],
    'odgovor3' : ['kosarka','košarka','кошарка','kosarci','košarci','кошарци','u kosarci','u košarci','у кошарци'],
    'odgovor4' : ['1991'],
    'odgovor5' : ['michael tyson','majk tajson','majkl tajson','мајкл тајсон','мајк тајсон'],
    'odgovor6' : ['united kingdom','ujedinjeno kraljevstvo','уједињено краљевство'],
    'odgovor7' : ['jna','stadion jna','стадион јна','јна'],
    'odgovor8' : ['nikola jokic','jokic','nikola jokić','jokić','никола јокић','јокић'],
    'odgovor9' : ['u skijanju','skijanju','skijanje','у скијању','скијању','скијање']
    
}
#Generisanje random brojeva za pitanje iz sporta.
randomNumberLak = random.randint(0,3)
randomNumberSrednji = random.randint(3,6)
randomNumberTezi = random.randint(6,10)

#Odvajanje vrednosti iz svih recnika pitanja i odgovora
vrednostiGeografija = list(pitanjaGeografija.values())
vrednostiIstorija = list(pitanjaIstorija.values())
vrednostiOpstaKultura = list(pitanjaOpstaKultura.values())
vrednostiSport = list(pitanjaSport.values())

vrednostiOdgovoriGeografija = list(odgovoriGeografija.values())
vrednostiOdgovoriIstorija = list(odgovoriIstorija.values())
vrednostiOdgovoriOpstaKultura = list(odgovoriOpstaKultura.values())
vrednostiOdgovoriSport = list(odgovoriSport.values())

#Petlje i varijable za laka pitanja u kvizu.
lakeVrednosti = []

for i in vrednostiGeografija[0:3]:
    lakeVrednosti.append(i)
for i in vrednostiIstorija[0:3]:
    lakeVrednosti.append(i)
for i in vrednostiOpstaKultura[0:3]:
    lakeVrednosti.append(i)
lakeVrednosti.append(vrednostiSport[randomNumberLak])

lakeVrednostiOdgovori = []

for i in vrednostiOdgovoriGeografija[0:3]:
    lakeVrednostiOdgovori.append(i)
for i in vrednostiOdgovoriIstorija[0:3]:
    lakeVrednostiOdgovori.append(i)
for i in vrednostiOdgovoriOpstaKultura[0:3]:
    lakeVrednostiOdgovori.append(i)
lakeVrednostiOdgovori.append(vrednostiOdgovoriSport[randomNumberLak])

#Petlje i varijable za pitanja srednje tezine u kvizu. 
srednjeVrednosti = []

for i in vrednostiGeografija[3:6]:
    srednjeVrednosti.append(i)
for i in vrednostiIstorija[3:6]:
    srednjeVrednosti.append(i)
for i in vrednostiOpstaKultura[3:6]:
    srednjeVrednosti.append(i)
srednjeVrednosti.append(vrednostiSport[randomNumberSrednji])

srednjeVrednostiOdgovori = []

for i in vrednostiOdgovoriGeografija[3:6]:
    srednjeVrednostiOdgovori.append(i)
for i in vrednostiOdgovoriIstorija[3:6]:
    srednjeVrednostiOdgovori.append(i)
for i in vrednostiOdgovoriOpstaKultura[3:6]:
    srednjeVrednostiOdgovori.append(i)
srednjeVrednostiOdgovori.append(vrednostiOdgovoriSport[randomNumberSrednji])

#Petlje i varijable za pitanja vece tezine u kvizu. 
tezeVrednosti = []

for i in vrednostiGeografija[6:9]:
    tezeVrednosti.append(i)
for i in vrednostiIstorija[6:9]:
    tezeVrednosti.append(i)
for i in vrednostiOpstaKultura[6:9]:
    tezeVrednosti.append(i)
tezeVrednosti.append(vrednostiSport[randomNumberTezi])

tezeVrednostiOdgovori = []

for i in vrednostiOdgovoriGeografija[6:9]:
    tezeVrednostiOdgovori.append(i)
for i in vrednostiOdgovoriIstorija[6:9]:
    tezeVrednostiOdgovori.append(i)
for i in vrednostiOdgovoriOpstaKultura[6:9]:
    tezeVrednostiOdgovori.append(i)
tezeVrednostiOdgovori.append(vrednostiOdgovoriSport[randomNumberTezi])

while True:
    brojTacnihOdgovora = 0
    brojPitanja = 1
    povecanjeVrednosti = 0
    odgovoriUcesnika = []

    ulaznoPitanje = input("Da li ste spremni za novu igru, d ili n?: ").lower()
    if ulaznoPitanje in ('d','д','да','da'):
        print('Izaberite tezinu pitanja.')
        print('1 za laka, 2 za srednja i 3 za teska')
        tezina = int(input('Unesite izbor: '))
        
        if tezina == 1:

            #for petlja za odredjivanje duzine same petlje.
            for i in range(10):

                #for petlja za prolazak kroz pitanja.
                for i in lakeVrednosti:
                    print('Pitanje broj', brojPitanja)
                    print(lakeVrednosti[povecanjeVrednosti])
                    odgovor = input("Vas odgovor: ").lower()
                    odgovoriUcesnika.append(odgovor)

                    if odgovor in (lakeVrednostiOdgovori[povecanjeVrednosti]):
                        brojTacnihOdgovora += 1
                    povecanjeVrednosti += 1
                    brojPitanja += 1
                break
            
        elif tezina == 2:

            #for petlja za odredjivanje duzine same petlje.
            for i in range(10):

                for i in srednjeVrednosti:
                    print('Pitanje broj', brojPitanja)
                    print(srednjeVrednosti[povecanjeVrednosti])
                    odgovor = input("Vas odgovor: ").lower()
                    odgovoriUcesnika.append(odgovor)

                    if odgovor in (srednjeVrednostiOdgovori[povecanjeVrednosti]):
                        brojTacnihOdgovora += 1
                    povecanjeVrednosti += 1
                    brojPitanja += 1
                break
               
        elif tezina == 3:
            
            #for petlja za odredjivanje duzine same petlje.
            for i in range(10):

                for i in tezeVrednosti:
                    print('Pitanje broj', brojPitanja)
                    print(tezeVrednosti[povecanjeVrednosti])
                    odgovor = input("Vas odgovor: ").lower()
                    odgovoriUcesnika.append(odgovor)

                    if odgovor in (tezeVrednostiOdgovori[povecanjeVrednosti]):
                        brojTacnihOdgovora += 1
                    povecanjeVrednosti += 1
                    brojPitanja += 1
                break
                
        else:
            print('Pogresan unos,pokusajte ponovo')
            continue

        # print('Vasi odgovori su: ', odgovoriUcesnika)

        #If i elif stejtmenti za kratku interakciju sa korisnikom.
        if brojTacnihOdgovora < 5:
            print("Broj tacnih odgovora je", brojTacnihOdgovora, ",vase opsto znanje je izuzetno slabo, nazad u klupe!")
        elif 10 > brojTacnihOdgovora > 5:
            print("Broj tacnih odgovora je", brojTacnihOdgovora, ",vase opsto znanje je na zavidnom nivou!")
        elif brojTacnihOdgovora == 10:
            print("Broj tacnih odgovora je", brojTacnihOdgovora, ",svaka cast, opsto znanje je savrseno!")

        print("Hvala sto se igrali nas kviz Ko ne zna, neka nauci!")

    elif ulaznoPitanje in ('n','н','ne','не'):
        print("Mnogo propustas!")
        break
    else:
        print("Pogresan unos, pokusajte ponovo.")
        continue