# Aceasta este sarcina pentru lecția despre conceptele avansate ale programării orientate pe obiecte în Python, cum ar fi super() și self, getter/setter și property, privatizarea și tipurile de metode.

from sigmoid_check.python_odyssey.lesson_14.lesson_14 import Lesson14

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.7
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.7

# VERIFICATION PROCESS
session = Lesson14()
# VERIFICATION PROCESS

"""
ISTORIA DIN SPATE:
O companie de tehnologie, TechSolutions, are nevoie de ajutorul nostru pentru a îmbunătăți gestionarea software-ului lor intern. 
Ei doresc să optimizeze modul în care tratează datele utilizatorilor și setările de sistem, 
respectând principiile OOP avansate pentru a asigura securitatea și modularitatea codului.
"""

"""
Pentru început vrem să asigurăm 3 tipuri de utilizatori în baza de date a companiei noastre.
Tipurile de utilizatori sunt:
1. Utilizator default - utilizatorul obișnuit care nu va avea careva drepturi de acces și va putea să utilizeze sistemul intern într-un mod limitat
2. Utilizator manager - utilizatorul care va avea drepturi de acces mai mari decât utilizatorul default și va putea să modifice setările de sistem, 
                        însă va avea restricții în ceea ce privește modificarea datelor utilizatorilor, 
                        fiind capabil doar să citească informația și nu să o modifice
3. Utilizator admin - utilizatorul care va avea toate drepturile de acces și va putea să modifice atât setările de sistem, cât și datele utilizatorilor

Iar din cauza faptului că nu dorim să replicăm aceleași metode de inițializare a utilizatorilor pentru fiecare tip de utilizator,
vrem să creăm o clasă de bază care să conțină metodele comune pentru toți utilizatorii și să moștenească aceste metode către clasele specifice tipurilor de utilizatori.

Ce trebuie să faci:
1. Creează o clasă `Utilizator` care să conțină un atribut public `nume` și un atribut protejat `_nivel_acces` cu valoarea implicită "Default".
    Clasa `Utilizator` trebuie să conțină metoda `afiseaza_nivel_acces` care să returneze string-ul "*nume-utilizator* are nivelul de acces *nivel-acces*.".
    De asemenea, clasa `Utilizator` trebuie să conțină metoda `utilizeaza_sistem` care să returneze string-ul "*nume-utilizator* poate utiliza funcții de bază ale sistemului.".

2. Creează o clasă `UtilizatorManager` care să moștenească clasa `Utilizator` și să aibă atributul protejat `_nivel_acces` cu valoarea "Manager".
    Clasa `UtilizatorManager` trebuie să conțină metoda `modifica_setari` care să returneze string-ul "*nume-utilizator* poate modifica setările sistemului.".
    De asemenea, clasa `UtilizatorManager` trebuie să conțină metoda `citeste_date_utilizator` care să returneze string-ul "*nume-utilizator* poate citi datele utilizatorilor.".

3. Creează o clasă `UtilizatorAdmin` care să moștenească clasa `Utilizator` și să aibă atributul protejat `_nivel_acces` cu valoarea "Admin".
    Clasa `UtilizatorAdmin` trebuie să conțină metoda `modifica_setari` care să returneze string-ul "*nume-utilizator* poate modifica setările sistemului.".
    De asemenea, clasa `UtilizatorAdmin` trebuie să conțină metoda `modifica_date_utilizator` care să returneze string-ul "*nume-utilizator* poate modifica datele utilizatorilor.".
"""

# CODUL TĂU VINE MAI JOS:
class Utilizator:
    def __init__(self, nume):
        self.nume = nume
        self._nivel_acces = "Default"

    def afiseaza_nivel_acces(self):
        return f"{self.nume} are nivelul de acces {self._nivel_acces}."

    def utilizeaza_sistem(self):
        return f"{self.nume} poate utiliza funcții de bază ale sistemului."

class UtilizatorManager(Utilizator):
    def __init__(self, nume):
        super().__init__(nume)
        self._nivel_acces = "Manager"

    def modifica_setari(self):
        return f"{self.nume} poate modifica setările sistemului."

    def citeste_date_utilizator(self):
        return f"{self.nume} poate citi datele utilizatorilor."

class UtilizatorAdmin(Utilizator):
    def __init__(self, nume):
        super().__init__(nume)
        self._nivel_acces = "Admin"

    def modifica_setari(self):
        return f"{self.nume} poate modifica setările sistemului."

    def modifica_date_utilizator(self):
        return f"{self.nume} poate modifica datele utilizatorilor."
# CODUL TĂU VINE MAI SUS:


# VERIFICATION PROCESS
print(session.check_task_1(Utilizator, UtilizatorManager, UtilizatorAdmin))
# VERIFICATION PROCESS

"""
Acum că am creat clasele de utilizatori, mai avem nevoie de însăși sistemul la care acești utilizatori vor avea acces.
Sistemul va conține o clasă `Sistem` care va conține o listă de utilizatori și metode pentru a adăuga utilizatori noi, a afișa utilizatorii existenți și a verifica nivelul de acces al unui utilizator.
La sistem va avea acces doar Utilizatorii Admin așa că trebuie să ne asigurăm că aceștia vor avea metode pentru a adăuga, a modificare și a șterge datele private ale sistemului.

Ce trebuie să faci:
1. Pentru această sarcină vom crea o copie a clasei `Utilizator` de mai sus, deoarece vom avea nevoie de aceeași structură pentru a adăuga utilizatorii în sistem.
   Creează o clasă `user` care să conțină un atribut privat `_nume` și un atribut protejat `__nivel_acces` cu valoarea implicită "Default".
   Acum avem nevoie de un getter și un setter pentru atributul `_nume` și `__nivel_acces` pentru a putea modifica aceste valori în afara clasei.

2. Creează o clasă `Sistem` care va conține un atribut privat `__utilizatori` inițializat cu un dicționar gol în care cheile vor fi id-ul și valorile utilizatorii.
    Clasa `Sistem` trebuie să conțină metoda `adauga_utilizator` care va primi un obiect de tip `Utilizator` și va adăuga utilizatorul la dicționar împreună cu un nou id.
    De asemenea, clasa `Sistem` trebuie să conțină metoda `afiseaza_utilizatori` care va returna o listă cu numele utilizatorilor existenți.
    Clasa `Sistem` trebuie să conțină metoda `verifica_nivel_acces` care va primi numele unui utilizator și va returna nivelul de acces al utilizatorului respectiv.
    Clasa `Sistem` trebuie să conțină și metoda `modifica_name_user` care va primi id-ul utilizatorului și noul nume al utilizatorului și va modifica numele utilizatorului respectiv.
    Clasa `Sistem` trebuie să conțină și metoda `sterge_utilizator` care va primi id-ul utilizatorului și va șterge utilizatorul respectiv.
    Clasa `Sistem` trebuie să conțină și metoda `modifica_nivel_acces` care va primi id-ul utilizatorului și noul nivel de acces al utilizatorului și va modifica nivelul de acces al utilizatorului respectiv.
"""

# CODUL TĂU VINE MAI JOS:
class user:
    def __init__(self, nume):
        self._nume = nume
        self.__nivel_acces = "Default"

    def get_nume(self):
        return self._nume

    def set_nume(self, nume):
        self._nume = nume

    def get_nivel_acces(self):
        return self.__nivel_acces

    def set_nivel_acces(self, nivel_acces):
        self.__nivel_acces = nivel_acces

class Sistem:
    def __init__(self):
        self.__utilizatori = {}

    def adauga_utilizator(self, utilizator):
        id_utilizator = len(self.__utilizatori) + 1
        self.__utilizatori[id_utilizator] = utilizator

    def afiseaza_utilizatori(self):
        return [utilizator.get_nume() for utilizator in self.__utilizatori.values()]

    def verifica_nivel_acces(self, nume_utilizator):
        for utilizator in self.__utilizatori.values():
            if utilizator.get_nume() == nume_utilizator:
                return utilizator.get_nivel_acces()
        return None

    def modifica_name_user(self, id_utilizator, nume_nou):
        if id_utilizator in self.__utilizatori:
            self.__utilizatori[id_utilizator].set_nume(nume_nou)

    def sterge_utilizator(self, id_utilizator):
        if id_utilizator in self.__utilizatori:
            del self.__utilizatori[id_utilizator]

    def modifica_nivel_acces(self, id_utilizator, nivel_acces_nou):
        if id_utilizator in self.__utilizatori:
            self.__utilizatori[id_utilizator].set_nivel_acces(nivel_acces_nou)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(user, Sistem))
# VERIFICATION PROCESS

# Task 3: Privatizarea
"""
Iar pe sfârșite a rămas ulimul element al sistemului nostru, vom aveae nevoie de o simulare a unei aplicații care va permite interacțiunea cu întregul sistem.

Ce trebuie să faci:
1. Creează o clasă `TechSolutionsApp` care va conține o valoare a clasei `versiune_applicatie` cu valoarea implicită "1.0".
    Această clasă va avea nevoie de 3 metode, fiecare dintre acestea va fi utilizată pentru a simula interacțiunea cu sistemul nostru.
    De asemenea clasa va primi ca argument la inițializare o valoare ce va reprezenta versiunea aplicatiei care va fi stocată în atributul `self.versiune_aplicatie`.

    Metoda `market_view` va fi o metodă statică care nu va avea acces la self sau cls și va returna string-ul "Vizualizare piață".
    Metoda `delogat_view` va fi o metodă de clasă care va avea acces la cls și va returna string-ul "Versiunea aplicației este *versiune-aplicatie*" utilizând atributul clasei.
    Metoda `account_view` va fi o metodă de instanță care va avea acces la self și va returna string-ul "Vizualizare aplicație user *versiune-aplicatie*" utilizând atributul instanței.
"""

# CODUL TĂU VINE MAI JOS:
class TechSolutionsApp:
    versiune_aplicatie = "1.0"

    def __init__(self, versiune_aplicatie):
        self.versiune_aplicatie = versiune_aplicatie

    @staticmethod
    def market_view():
        return "Vizualizare piață"

    @classmethod
    def delogat_view(cls):
        return f"Versiunea aplicației este {cls.versiune_aplicatie}"

    def account_view(self):
        return f"Vizualizare aplicație user {self.versiune_aplicatie}"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(TechSolutionsApp))
print(session.get_completion_percentage())
# VERIFICATION PROCESS
#Tema p-u acasă (TPA) a fost realizată de Maxim Papanaga :D