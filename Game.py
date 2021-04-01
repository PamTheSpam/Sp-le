from texttable import Texttable
import csv
import string
import sys
import time


start = time.time()

vārdi = open("words.txt", 'r')
reader = csv.reader(vārdi)
allRows = [row for row in reader]

Vārds = input("Tavs vārds: ")

table = Texttable()
list1 = [1, "Z", "A", "M", "A", "T", "N", "I", "E", "K", "U", "-", "N", "A", "M", "S", "T", "-"]
list2 = [2, "I", "R", "O", "Ž", "U", "-", "L", "A", "U", "K", "U", "M", "S", "M", "S", "T", "R"]
list3 = [3, "E", "Ā", "D", "M", "Z", "R", "S", "R", "D", "A", "Ā", "O", "O", "Ī", "T", "O", "D"]
list4 = [4, "M", "S", "S", "A", "Ā", "R", "Z", "O", "D", "O", "Z", "A", "Ā", "L", "A", "S", "S"]
list5 = [5, "E", "R", "-", "S", "S", "P", "D", "K", "U", "K", "O", "K", "S", "E", "D", "T", "K"]
list6 = [6, "Ļ", "Ā", "Z", "P", "O", "A", "A", "D", "Ā", "-", "R", "S", "D", "S", "I", "A", "O"]
list7 = [7, "U", "S", "Z", "O", "Ā", "S", "B", "Ā", "R", "R", "O", "M", "S", "T", "O", "S", "K"]
list8 = [8, "-", "D", "I", "K", "N", "V", "A", "D", "U", "-", "M", "O", "L", "Ī", "N", "-", "-"]
list9 = [9, "M", "O", "D", "U", "Z", "S", "S", "M", "R", "O", "D", "Ā", "Z", "B", "S", "P", "S"]
list10 = [10, "O", "K", "A", "K", "P", "A", "-", "A", "-", "T", "I", "L", "T", "A", "-", "R", "A"]
list11 = [11, "L", "M", "Ā", "O", "D", "S", "M", "M", "D", "S", "Ā", "S", "R", "S", "O", "O", "B"]
list12 = [12, "S", "R", "S", "K", "D", "A", "Ā", "M", "S", "M", "Ā", "M", "S", "-", "L", "M", "Ī"]
list13 = [13, "I", "R", "S", "S", "Z", "D", "J", "A", "D", "A", "M", "M", "O", "K", "I", "E", "T"]
list14 = [14, "Ž", "Z", "A", "D", "O", "O", "A", "S", "Z", "S", "S", "Ā", "R", "O", "M", "N", "S"]
list15 = [15, "A", "D", "R", "A", "I", "Ņ", "A", "-", "P", "A", "R", "K", "S", "K", "P", "Ā", "E"]
list16 = [16, "-", "R", "D", "Ā", "Z", "R", "D", "D", "D", "Ā", "R", "M", "D", "S", "I", "D", "L"]
list17 = [17, "A", "L", "P", "Ī", "N", "I", "S", "M", "A", "-", "S", "I", "E", "N", "J", "E", "Ī"]
list18 = [18, "A", "L", "P", "Ī", "N", "I", "S", "M", "A", "-", "S", "I", "E", "N", "A", "T", "M"]
list19 = [19, "A", "L", "R", "D", "-", "P", "O", "R", "T", "S", "-", "S", "A", "-", "A", "K", "S"]




table.header(["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R"])
table.add_row(list1)
table.add_row(list2)
table.add_row(list3)
table.add_row(list4)
table.add_row(list5)
table.add_row(list6)
table.add_row(list7)
table.add_row(list8)
table.add_row(list9)
table.add_row(list10)
table.add_row(list11)
table.add_row(list12)
table.add_row(list13)
table.add_row(list14)
table.add_row(list15)
table.add_row(list16)
table.add_row(list17)
table.add_row(list18)
table.add_row(list19)

print(table.draw())


B2M2 = allRows[0]
A1A12 = allRows[1]
G5G14 = allRows[2]
O2O18 = allRows[3]
C15M15 = allRows[4]
A18O18 = allRows[5]
R18R4 = allRows[6]
P3P17 = allRows[7]
B1O1 = allRows[8]
R19E19 = allRows[9]
D5D13 = allRows[10]

answerList = ["B2M2", "A1A12", "G5G14", "O2O18", "C15M15", "A18O18", "R18R4", "P3P17", "B1O1", "R19E19", "D5D13"]
koordinātuSaraksts = []


RkoordSaraksts = []
OkoordSaraksts = []
MkoordSaraksts = []
AkoordSaraksts = []
SkoordSaraksts = []

DkoordSaraksts = []
ĀkoordSaraksts = []
RkoordSaraksts = []
ZkoordSaraksts = []
SkoordSaraksts = ["D5"]

lietotieBurti = []

print("")
print('''Vārdi kas jāatrod:ZIEMEĻU MOLS
                  ALPĪNISMA SIENA
                  ROŽU LAUKUMS
                  DABAS MĀJA
                  STADIONS OLIMPIJA
                  RAIŅA PARKS
                  MĪLESTĪBAS KOKS
                  OSTAS PROMENĀDE
                  AMATNIEKU NAMS
                  SPOKU KOKS
''')

minejums1 = input("Kurās koordinātēs atrodas vārds?")
if minejums1 in answerList:
    koordinātuSaraksts.append(minejums1)

    if minejums1 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

      
    if minejums1 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums1 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums1 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums1 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums1 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums1 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums1 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums1 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums1 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")

    if minejums1 == "D5D13":
        print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
                
    



minejums2 = input("Kurās koordinātēs atrodas vārds? ")
if minejums2 in answerList:
    koordinātuSaraksts.append(minejums2)
    if minejums2 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

      
    if minejums2 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums2 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums2 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums2 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums2 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums2 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums2 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums2 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums2 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")

    if minejums2 == "D5D13":
        print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    
    

minejums3 = input("Kurās koordinātēs atrodas vārds? ")
if minejums3 in answerList:
    koordinātuSaraksts.append(minejums3)

    if minejums3 == "D5D13":
        print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    

    if minejums3 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

      
    if minejums3 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums3 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums3 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums3 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums3 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums3 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums3 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums3 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums3 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")
    
    
    

minejums4 = input("Kurās koordinātēs atrodas vārds? ")
if minejums4 in answerList:
    koordinātuSaraksts.append(minejums4)

    if minejums4 == "D5D13":
        print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    

    if minejums4 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

      
    if minejums4 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums4 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums4 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums4 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums4 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums4 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums4 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums4 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums4 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")
    
    


minejums5 = input("Kurās koordinātēs atrodas vārds? ")
if minejums5 in answerList:
    koordinātuSaraksts.append(minejums5)

    if minejums5 == "D5D13":
        print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    

    if minejums5 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

      
    if minejums5 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums5 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums5 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums5 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums5 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums5 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums5 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums5 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums5 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")
    
    
    


minejums6 = input("Kurās koordinātēs atrodas vārds? ")
if minejums6 in answerList:
    koordinātuSaraksts.append(minejums6)

    if minejums6 == "D5D13":
        print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    

    if minejums6 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

      
    if minejums6 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums6 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums6 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums6 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums6 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums6 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums6 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums6 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if minejums6 == "D5":
            print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
            print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    

        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums6 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")
    
    

minejums7 = input("Kurās koordinātēs atrodas vārds? ")
if minejums7 in answerList:
    koordinātuSaraksts.append(minejums7)

    if minejums7 == "D5D13":
        print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    

    if minejums7 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

      
    if minejums7 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums7 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums7 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums7 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums7 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums7 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums7 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums7 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums7 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")
    
    

minejums8 = input("Kurās koordinātēs atrodas vārds? ")
if minejums8 in answerList:
    koordinātuSaraksts.append(minejums8)

    if minejums8 == "D5D13":
        print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    

    if minejums8 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

      
    if minejums8 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums8 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums8 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums8 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums8 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums8 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums8 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums8 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums8 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")
    
    

minejums9 = input("Kurās koordinātēs atrodas vārds? ")
if minejums9 in answerList:
    koordinātuSaraksts.append(minejums9)

    if minejums9 == "D5D13":
        print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    

    if minejums9 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

      
    if minejums9 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums9 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums9 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums9 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums9 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums9 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums9 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums9 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums9 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")
    
    
minejums10 = input("Kurās koordinātēs atrodas vārds? ")
if minejums10 in answerList:
    koordinātuSaraksts.append(minejums10)

    if minejums10 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

        if minejums10 == "D5":
            print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    
      
    if minejums10 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums10 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums10 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums10 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums10 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums10 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums10 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums10 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums10 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()


        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")

        if minejums1 == "A1A12":
            print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
            print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums1 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums1 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

        if minejums10 == "D5D13":
            print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")

    if minejums1 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums1 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums1 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums1 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums1 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums1 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")
    

    
minejums11 = input("Kurās koordinātēs atrodas vārds? ")
if minejums11 in answerList:
    koordinātuSaraksts.append(minejums10)

    if minejums2 == "D5D13":
        print('''“Spoku koks” veltīts latviešu leģendārajai rokgrupai “Līvi”  “Spoku koks” ir sešus metrus augsts koks, kas veidots no četriem tūkstošiem metāla stienīšu.Te var pasēdēt uz soliņiem, kas veidoti ģitāras grifa formā, un, nospiežot pogu, atskaņot tautā iemīļotās grupas “Līvi” dziesmas.''')
        print()
        if "D5" in SkoordSaraksts:
            time.sleep(1)
            
        if "D5" not in SkoordSaraksts:
            SkoordSaraksts.append("D5")
    

    if minejums11 == "B2M2":
        print('''Rožu laukums- Rožu laukums ir pilsētas sirds un satikšanās vieta. Atbilstoši nosaukumam tā nemainīga vērtība ir rozes, kas šeit tiek stādītas jau vairāk nekā simts gadus.''')
        print()

        if "B2" in RkoordSaraksts:
            time.sleep(1)

        if "B2" not in RkoordSaraksts:
            RkoordSaraksts.append("B2")

      
    if minejums11 == "A1A12":
        print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
        print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums11 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums11 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums11 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums11 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums11 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums11 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums11 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums11 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()


        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")

        if minejums11 == "A1A12":
            print('''Ziemeļu mols-Latvijā garākais mols – Ziemeļu mols – būvēts 19. gadsimta beigās kā ļoti svarīga Liepājas Jūras cietokšņa un militārās ostas daļa. Mola garums ir 1800 metri, platums – 7,35 metri.''')
            print()

        if "A1" in ZkoordSaraksts:
            time.sleep(1)
            
        if "A1" not in ZkoordSaraksts:
            ZkoordSaraksts.append("A1")

    if minejums11 == "G5G14":
        print('''Dabas māja ir vides un dabas izglītības centrs, kuru var apmeklēt skolēnu grupas un citi interesenti, piesakoties ekskursijām, lai aizraujošā un saistošā veidā izpētītu dabas procesus.''')
        print()
        if "G5" in DkoordSaraksts:
            time.sleep(1)
            
        if "G5" not in DkoordSaraksts:
            DkoordSaraksts.append("G5")

    if minejums11 == "O2O18":
        print('''Stadions "Olimpija"- Deviņdesmito gadu sākumā šajā stadionā tika rīkoti gan stadiona motokrosi, gan autosacīkstes. Stadions paredzēts, lai pulcētu futbola spēlētājus un šī sporta veida fanus vienuviet.''')
        print()
        if "O2" in SkoordSaraksts:
            time.sleep(1)
            
        if "O2" not in SkoordSaraksts:
            SkoordSaraksts.append("O2")

    if minejums11 == "C15M15":
        print('''Raiņa parks-Raiņa parks aizņem 15,5 hektārus lielu zemes gabalu starp Zemnieku, Brīvības, Parka un Tirgus ielu, kas to šķērso dienvidgalā. Līdz 19. gadsimta 30. gadiem tur bija purvaina pļava un alkšņu mežiņš. ''')
        print()
        if "C15" in RkoordSaraksts:
            time.sleep(1)
            
        if "C15" not in RkoordSaraksts:
            RkoordSaraksts.append("C15")

    if minejums11 == "A18O18":
        print('''Alpīnisma siena- atrodas Liepājas Olimpiskā centra manēžā. Alpīnisma sienā var pārbaudīt savus spēkus klinšu kāpšanā. ''')
        print()
        if "A18" in AkoordSaraksts:
            time.sleep(1)
            
        if "A18" not in AkoordSaraksts:
            AkoordSaraksts.append("A18")

    if minejums11 == "R18R4":
        print('''Mīlestības koks- šī ir vieta, kur jaunlaulātie var pieslēgt slēdzenes kā apliecinājumu mūžīgai mīlestībai. Tas ir 4 metrus augsts un 2,4 metrus plats. ''')
        print()
        if "R18" in MkoordSaraksts:
            time.sleep(1)
            
        if "R18" not in MkoordSaraksts:
            MkoordSaraksts.append("R18")
    if minejums11 == "P3P17":
        print('''Ostas promenāde- Padomju gados te bija slēgta zona. Šobrīd Promenāde ir izveidojusies par jauku pastaigu vietu dienā un atraktīvu nakts dzīves centru vakara stundās. No Promenādes paveras burvīgs skats uz ostas piestātnēm, kuģiem un jahtām. Ostas promenādi rotā Dzintara pulkstenis''')
        print()
        if "P3" in OkoordSaraksts:
            time.sleep(1)
            
        if "P3" not in OkoordSaraksts:
            OkoordSaraksts.append("P3")
    if minejums11 == "B1O1":
        print('''Amantnieku namā iespējams apskatīt gan to, kā uz stellēm top tautas tērpi, gan to, kā tiek veidotas lelles, sveces, metāla rotas, keramikas darbi, ādas un dzintara izstrādājumi. Amatnieku namā arī apskatāmas garākās dzintara krelles Latvijā. Tās ir 123 metru garas, 19,5 kilogramu smagas, ar teju 17 000 dzintara gabaliņiem''')
        print()
        if "B1" in AkoordSaraksts:
            time.sleep(1)
            
        if "B1" not in AkoordSaraksts:
            AkoordSaraksts.append("B1")
    if minejums11 == "R19E19":
        print('''"SKAŅAS STROPS" - Telpiski veidotais strops jeb vijums tapis iedvesmojoties no mūzikas skaņām. No necilas skices uz mana darba galda tas izaudzis līdz spilgtam apjomam, kas no šodienas rotās pilsētas panorāmu.''')
        print()
        if "R19" in SkoordSaraksts:
            time.sleep(1)
            
        if "R19" not in SkoordSaraksts:
            SkoordSaraksts.append("R19")
    
    
        
        



print("Tev ir jāuzraksta vārds 'Romas Dārzs'")

rKoord = input("Kurās koordinātēs atrodās burts 'R': ")
if rKoord in RkoordSaraksts:
    print("Pareizi, tā tik turpināt!")


if rKoord not in RkoordSaraksts:
    print("Nav pariezās koordinātes. Mēģini vēlriez.")
    sys.exit()

oKoord = input("Kurās koordinātēs atrodās burts 'O': ")
if oKoord in OkoordSaraksts:
    print("Pariezi!")

if oKoord not in OkoordSaraksts:
    print("Nav pariezās koordinātes. Mēģini vēlreiz.")
    sys.exit()

mKoord = input("Kurās koordinātēs atrodās burts 'M': ")
if mKoord in MkoordSaraksts:
    print("Pareizi, tā tik turpināt!")

if mKoord not in MkoordSaraksts:
    print("Nav pariezās koordinātes. Mēģini vēlriez.")
    sys.exit()

aKoord = input("Kurās koordinātēs atrodās burts 'A': ")
if aKoord in AkoordSaraksts:
    print("Pareizi, tā tik turpināt!")

if aKoord not in AkoordSaraksts:
    print("Nav pariezās koordinātes. Mēģini vēlriez.")
    sys.exit()

AkoordSaraksts.remove(aKoord)



sKoord = input("Kurās koordinātēs atrodās burts 'S': ")
if sKoord in SkoordSaraksts:
    print("Pareizi, tā tik turpināt!")

if sKoord not in SkoordSaraksts:
    print("Nav pariezās koordinātes. Mēģini vēlriez.")
    sys.exit()

SkoordSaraksts.remove(sKoord)

dKoord = input("Kurās koordinātēs atrodās burts 'D': ")
if dKoord in DkoordSaraksts:
    print("Pareizi, tā tik turpināt!")

if dKoord not in DkoordSaraksts:
    print("Nav pariezās koordinātes. Mēģini vēlriez.")
    sys.exit()

aKoord = input("Kurās koordinātēs atrodās burts 'Ā': ")
if aKoord in AkoordSaraksts:
    atiblide = input("Vai vēlaties pievienot mīkstinājuma zīmi? (Y/N)")
    if atiblide == "Y":
        print("Pareizi, tā tik turpināt!")
    if atiblide == "N":
        print("Nepariezi. Mēģini vēlriez.")
        sys.exit()
    
if aKoord not in AkoordSaraksts:
    print("Nav pariezās koordinātes. Mēģini vēlriez.")
    sys.exit()

rKoord = input("Kurās koordinātēs atrodās burts 'R': ")
if rKoord in RkoordSaraksts:
    print("Pareizi, tā tik turpināt!")

if rKoord not in RkoordSaraksts:
    print("Nav pariezās koordinātes. Mēģini vēlriez.")
    sys.exit()

RkoordSaraksts.remove(rKoord)

zKoord = input("Kurās koordinātēs atrodās burts 'Z': ")
if zKoord in ZkoordSaraksts:
    print("Pareizi, tā tik turpināt!")

if zKoord not in ZkoordSaraksts:
    print("Nav pariezās koordinātes. Mēģini vēlriez.")
    sys.exit()

sKoord = input("Kurās koordinātēs atrodās burts 'S': ")
if sKoord in SkoordSaraksts:
    print("Apsviecu! Esi uzvarējis!!")
    end = time.time()
    print("Apsveicu " + Vārds + ". Tu esi uzvarējis!!!")
    print('Tu spēlēji: ', end - start, 'sekundes')

if sKoord not in SkoordSaraksts:
    print("Nav pariezās koordinātes. Mēģini vēlriez.")
    sys.exit()

