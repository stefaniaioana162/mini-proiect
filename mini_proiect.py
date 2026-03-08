# Mini-proiect: Cainareanu Ioana-Stefania


import json
'''
Acest proiect reprezinta o evidenta a angajatilor unei companii.
In cadrul acestui proiect se vor folosi conceptele de:
1. Structuri de date 
2. Functii 
3. Lucrul cu fisiere
4. Excepții (blocul try-except)
5. Modulul json (citire/scriere date in format JSON)

'''
evidenta_angajati = {
    "1234567890123": {
        "nume": "Popa",
        "prenume": "Lucian",
        "varsta": 25,
        "salar": 4050,
        "departament": "Logistica",
        "senioritate": "junior"
    },
    "2876543210123": {
        "nume": "Hutanu",
        "prenume": "Adriana",
        "varsta": 40,
        "salar": 5000,
        "departament": "HR",
        "senioritate": "mid"
    },
    "3567890123456": {
        "nume": "Bant",
        "prenume": "Alexandra",
        "varsta": 32,
        "salar": 6000,
        "departament": "IT",
        "senioritate": "senior"
    },
    "4890123456789": {
        "nume": "Faibis",
        "prenume": "Andrei",
        "varsta": 28,
        "salar": 4500,
        "departament": "Marketing",
        "senioritate": "mid"
    },
    "5123456789012": {
        "nume": "Dumitrescu",
        "prenume": "Andreea",    
        "varsta": 28,
        "salar": 4100,
        "departament": "Productie",
        "senioritate": "junior"
    },
    "6456789012345": {
        "nume": "Popescu",
        "prenume": "Ioana",
        "varsta": 35,
        "salar": 5500,
        "departament": "Finante",
        "senioritate": "senior"
    },
    "7789012345678": {
        "nume": "Ciubotaru",
        "prenume": "Cristina",
        "varsta": 47,
        "salar": 4800,
        "departament": "Resurse Umane",
        "senioritate": "senior"    
    },
    "8012345678901": {
        "nume": "Marinescu",
        "prenume": "Alexandru",
        "varsta": 32,
        "salar": 5200,
        "departament": "IT",
        "senioritate": "senior"
    },   
    
}



def adauga_angajat():
    '''
    Adaugare angajat.
    
    Args:
        - cnp(str): CNP-ul angajatului
        - nume(str): Numele angajatului
        - prenume(str): Prenumele angajatului
        - varsta(int): Varsta angajatului
        - salar(int): Salariul angajatului
        - departament(str): Departamentul angajatului
        - senioritate(str): Senioritatea angajatului(junior, mid, senior)
    
    Returns:
        None
    '''
    nume = input('Nume: ')
    prenume = input('Prenume: ')
    varsta = int(input('Varsta: '))
    salar = int(input('Salar: '))
    departament = input('Departament: ')
    senioritate = input('Senioritate: ')
    cnp = input('CNP: ')
    evidenta_angajati[cnp] = {
        "nume": nume,
        "prenume": prenume,
        "varsta": varsta,
        "salar": salar,
        "departament": departament,
        "senioritate": senioritate
    }
    print(f'Noul angajat {nume} {prenume} a fost adaugat!')
    
    
    
def cautare_angajat():
    '''
    Cautare angajat dupa CNP si afisarea informatiilor acestuia.
    
    Args:
        - cnp(str): CNP-ul angajatului de cautat
        
    Returns:
        None
    '''
    cnp = input('Introdu CNP: ')
    if cnp in evidenta_angajati:
        angajat = evidenta_angajati[cnp]
        print(f'Informatii despre angajatul cu CNP: {cnp}: ')
        print(f'Nume: {angajat['nume']} Prenume: {angajat['prenume']}')
        print(f'Varsta: {angajat['varsta']} ani')
        print(f'Salar: {angajat['salar']}')
        print(f'Departament: {angajat['departament']}')
        print(f'Senioritate: {angajat['senioritate']}')
    else:
        print(f'Angajatul nu a fost gasit.')
        
        
           
def modificare_angajat():
    '''
    Modificare date angajat dupa CNP.
    
    Args:
        - cnp(str): CNP-ul angajatului de modificat
        - nume(str, optional): Noul nume al angajatului. Default este None.
        - prenume (str, optional): Noul prenume al angajatului. Default este None.
        - varsta (int, optional): Noua varsta a angajatului. Default este None.
        - salar (int, optional): Noul salar al angajatului. Default este None.
        - departament (str, optional): Noul departament al angajatului. Default este None.
        - senioritate (str, optional): Noua senioritate a angajatului. Default este None.
        
    Returns:
        None
    '''
    cnp = input('Introdu CNP: ')
    if cnp in evidenta_angajati:
        angajat = evidenta_angajati[cnp]
        print(f'Modifica datele angajatului {angajat['nume']} {angajat['prenume']}')
        nume = input('Modifica nume: ')
        prenume = input('Modifica prenume: ')
        varsta = input('Modifica varsta: ')
        salar = input('Modifica salar: ')
        departament = input('Modifica departament: ')
        senioritate = input('Modifica senioritate: ')
        if nume:
            angajat['nume'] = nume
        if prenume:
            angajat['prenume'] = prenume
        if varsta:
            angajat['varsta'] = varsta
        if salar:
            angajat['salar'] = salar
        if departament:
            angajat['departament'] = departament
        if senioritate:
            angajat['senioritate'] = senioritate
        print(f'Datele angajatului cu CNP: {cnp} au fost modificate.')
    else:
        print(f'Angajatul nu a fost gasit.')
        
        
        
def stergere_angajat():
    '''
    Stergerea unui angajat dupa CNP.
    
    Args:
        - cnp(str): CNP-ul angajatului de sters
        
    Returns:
        None
    '''
    cnp = input('Introdu CNP: ')
    if cnp in evidenta_angajati:
        angajat = evidenta_angajati[cnp]
        del evidenta_angajati[cnp]
        print(f'Angajatul {angajat['nume']} {angajat['prenume']} cu CNP: {cnp } a fost sters.')
    else:
        print(f'Angajatul cu CNP: {cnp} nu a fost gasit.')
        
        
        
def afisare_angajati():
    '''
    Afisarea tuturor angajatilor.
    
    Returns:
        None
    '''
    #print(json.dumps(evidenta_angajati, indent=4))
    if evidenta_angajati:
        for cnp, angajat in evidenta_angajati.items():
            print(f'CNP: {cnp}')
            print(f'Nume: {angajat['nume']} Prenume: {angajat['prenume']}')
            print(f'Varsta: {angajat['varsta']}')
            print(f'Salar: {angajat['salar']}')
            print(f'Departament: {angajat['departament']}')
            print(f'Senioritate: {angajat['senioritate']}')
            print(" ")
            
            
            
def calcul_total__salarii_companie():
    '''
    Calcularea costului total al salariilor pentru companie.
    
    Returns:
        None
    '''
    calcul = sum(angajat['salar'] for angajat in evidenta_angajati.values())
    print(f'Calcul cost total salarii companie: {calcul} RON')
    
    
    
def calcul_total_salarii_departament():
    '''
    Calcularea costului total al salariilor pentru un anumit departament.
    
    Returns:
        None
    '''
    departament = input('Introdu departamentul: ')
    calcul_deparatment = sum(angajat['salar'] for angajat in evidenta_angajati.values() if angajat['departament'].lower() == departament.lower())
    print(f'Calcul cost total salarii pentru departamentul {departament}: {calcul_deparatment} RON')
    
    
    
def afisare_angajati_pe_baza_senioritate():
    '''
    Afisarea angajatilor pe baza senioritatii.
        - senioritate(str): Senioritatea pentru care se afiseaza angajatii(junior, mid, senior)
        
    Returns:
        None
    '''
    senioritate = input('Introdu senioritate: ')
    angajati_senioritate = [angajat for angajat in evidenta_angajati.values() if angajat['senioritate'] == senioritate]
    for angajat in angajati_senioritate:
        print(f'Nume: {angajat['nume']} Prenume: {angajat['prenume']}')
        print(f'Varsta: {angajat['varsta']}')
        print(f'Salar: {angajat['salar']}')
        print(f'Departament: {angajat['salar']}')
        print(" ")
        
        
        
def afisare_angajati_pe_baza_departament():
    '''
    Afisarea angajatilor pe baza departamentului:
    
    Args:
        - departament(str): Departamentul pentru care se afiseaza angajatii.
        
    Returns:
        None
    '''
    departament = input('Introdu departamentul: ')
    angajati_departament = [angajat for angajat in evidenta_angajati.values() if angajat['departament'].lower() == departament.lower()]
    for angajat in angajati_departament:
        print(f'Nume: {angajat['nume']} Prenume: {angajat['prenume']}')
        print(f'Vartsa: {angajat['varsta']}')
        print(f'Salar: {angajat['salar']}')
        print(f'Senioritate: {angajat['senioritate']}')
        print(" ")
        
        
  
        

while True:
    '''
    Meniu pentru a alege actiunea dorita.
    
    Returns:
        None
    '''
    optiune = input('Alege optiune: ').lower()
    if optiune == 'iesire':
        print('Ai iesit din program')
        break
    if optiune == 'adaugare angajat':
        adauga_angajat()
    if optiune == 'cautare angajat':
        cautare_angajat()
    if optiune == 'modificare date':
        modificare_angajat()
    if optiune == 'stergere angajat':
        stergere_angajat()
    if optiune == 'afisare angajati':
        afisare_angajati()
    if optiune == 'calcul total salarii companie':
        calcul_total__salarii_companie()
    if optiune == 'calcul total salarii departament':
        calcul_total_salarii_departament()
    if optiune == 'afisare angajati pe baza senioritatii':
        afisare_angajati_pe_baza_senioritate()
    if optiune == 'afisare angajati pe baza departamentului':
        afisare_angajati_pe_baza_departament()
 
        



# Error Handling: blocul try-except

try:
    '''
    Citirea datelor din fisierul informatii_angajati.json si afisarea acestora.
    Daca fisierul nu exista, se va afisa un mesaj de eroare.
    
    Returns:
        None
    '''
    with open('informatii_angajati.json', 'r') as my_project:
        print(my_project.read())
except FileNotFoundError:
    print('Fisierul informatii_angajati.json nu exista!')
else:
    print('Fisierul a fost deschis cu succes!')
        
# informatii_angajati.json - fisierul in care sunt stocate informatiile despre angajati pentru a putea fi accesate si modificate      

    

  

        
    
    