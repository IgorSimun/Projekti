#!/usr/bin/env python3
"""
Sorting out audio devices in groups,checking for newer versions and calling as arguments.

@date 2022-10-12
@author Igor Simunovic <igorsimunovic2@gmail.com>
"""
import argparse
allVersion =[
'MAIN_MIB3MP_AU_ER_G4x_2203602',
'MAIN_MIB3H_AU_ER_G4x_2203601',
'MAIN_MIB3P_PO_ER_G4x_2203705',
'MAIN_MIB3P_AU_ER_G4x_2203608',
'MAIN_MIB3MP_AU_ER_G4x_2203705',
'MAIN_MIB3P_PO_ER_G4x_2203602',
'MAIN_MIB3H_AU_ER_G4x_2203803',
'MAIN_MIB3P_AU_ER_G4x_2203806',
'MAIN_MIB3MP_AU_ER_G4x_2203900',
'MAIN_MIB3H_AU_ER_G4x_2203904',
'MAIN_MIB3P_AU_ER_G4x_2203705',
'MAIN_MIB3P_PO_ER_G4x_2203803',
'MAIN_MIB3H_AU_ER_G4x_2203702',
'MAIN_MIB3MP_AU_ER_G4x_2203801',
'MAIN_MIB3P_AU_ER_G4x_2203903',
'MAIN_MIB3P_PO_ER_G4x_2203904']
allVersion.sort()

def findAudiPremium():
    matches = [match for match in allVersion if "MIB3P_AU" in match]
    return matches
def findAudiElectric():
    matches = [match for match in allVersion if "MIB3MP_AU" in match]
    return matches
def findAudiHigh():
    matches = [match for match in allVersion if "MIB3H_AU" in match]
    return matches
def findPorsche():
    matches = [match for match in allVersion if "MIB3P_PO" in match]
    return matches
def checkAudiPremium():
    x = findAudiPremium()
    audiPremium = 'MAIN_MIB3P_AU_ER_G4x_2203903'
    if x[-1][-7:-2] == audiPremium[-7:-2] or x[-1][-7:-2] < audiPremium[-7:-2]:
        print('There is no newer version for Audi Premium.')
        print('Current version for Audi Premium is {}'.format(audiPremium))
    else:
        print('There is newer version for Audi Premium.')
        print('Current version for Audi Premium is {}'.format(audiPremium))
        print('Newer version for Audi Premium is {}'.format(x[-1]))
def checkAudiElectric():
    x = findAudiElectric()
    audiElectric = 'MAIN_MIB3MP_AU_ER_G4x_2203803'
    if x[-1][-7:-2] == audiElectric[-7:-2] or x[-1][-7:-2] < audiElectric[-7:-2]:
        print('There is no newer version for Audi Electric.')
        print('Current version for Audi Electric is {}'.format(audiElectric))
    else:
        print('There is newer version for Audi Electric')
        print('Current version on board for Audi Electric is {}'.format(audiElectric))
        print('Newer version for Audi Electric is {}'.format(x[-1]))
def checkAudiHigh():
    x = findAudiHigh()
    audiHigh = 'MAIN_MIB3H_AU_ER_G4x_2203902'
    if x[-1][-7:-2] == audiHigh[-7:-2] or x[-1][-7:-2] < audiHigh[-7:-2]:
        print('There is no newer version for Audi High.')
        print('Current version for Audi High is {}'.format(audiHigh))
    else:
        print('There is newer version for Audi High.')
        print('Current version for Audi High is {}'.format(audiHigh))
        print('Newer version for Audi High is {}'.format(x[-1]))

def checkPorsche():
    x = findPorsche()
    Porsche = 'MAIN_MIB3P_PO_ER_G4x_2203804'
    if x[-1][-7:-2] == Porsche[-7:-2] or x[-1][-7:-2] < Porsche[-7:-2]:
        print('There is no newer version for Porsche')
        print("Current version on Porsche board is: {}.".format(Porsche))
    else:
        print("There is a newer version for Porsche.")
        print("Current version on Porsche board is: {}.".format(Porsche))
        print("Newer version for Porsche is {}.".format(x[-1]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ap','--premium',help='calls checkAudiPremium function',action='store_true')
    parser.add_argument('-ae','--electric',help='calls checkAudiElectric function',action='store_true')
    parser.add_argument('-ah','--high',help='calls checkAudiHigh function',action='store_true')
    parser.add_argument('-p','--porsche',help='calls checkPorsche function',action='store_true')
    parser.add_argument('-e','--everything',help='calls all functions with single argument',action='store_true')
    args = parser.parse_args()

    premium = args.premium
    electric = args.electric
    high = args.high
    porsche = args.porsche
    everything = args.everything


    if premium and not everything:
        checkAudiPremium()
    if  electric and not everything:
        checkAudiElectric()
    if high and not everything:
        checkAudiHigh()
    if args.porsche and not everything:
        checkPorsche()
    if everything:
        checkAudiPremium()
        checkAudiElectric()
        checkAudiHigh()
        checkPorsche()



#checkAudiPremium()
#checkAudiElectric()
#checkAudiHigh()
#checkPorsche()
#findAudiPremium()
#findAudiElectric()
#findAudiHigh()
#findPorsche()


#audiPremium = MIB3P_AU
#audiElectric = MIB3MP_AU
#audiHigh = MIB3H_AU
#porsche = MIB3P_PO
#Audi premium:      MAIN_MIB3P_AU_ER_G4x_2203903
#Audi electric:     MAIN_MIB3MP_AU_ER_G4x_2203803
#Audi high:         MAIN_MIB3H_AU_ER_G4x_2203902
#Porsche:           MAIN_MIB3P_PO_ER_G4x_2203804