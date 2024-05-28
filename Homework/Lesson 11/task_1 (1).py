from sigmoid_check.python_odyssey.lesson_11.lesson_11 import Lesson11

# Această temă pentru acasă necesită instalarea librăriei `sigmoid_check` cu versiunea cel puțin 0.0.4
# Pentru a instala această librărie, rulați următorul cod în terminal:
# pip install sigmoid_check==0.0.4

# VERIFICATION PROCESS
session = Lesson11()
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_1` care poate primi un număr variabil de argumente și returnează suma acestora.
Exemplu: task_1(1, 2, 3) ➞ 6
"""

# CODUL TĂU VINE MAI JOS:
def task_1(*args):
    return sum(args)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_1(task_1))
# VERIFICATION PROCESS


"""
Task: Creați o funcție cu numele `task_2` care primește un număr variabil de argumente și returnează o listă cu argumentele care sunt numere întregi.
Exemplu: task_2(1, 2, 'a', 'b') ➞ [1, 2]
"""

# CODUL TĂU VINE MAI JOS:
def task_2(*args):
    return [arg for arg in args if isinstance(arg, int)]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_2(task_2))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_3` care poate primi un număr variabil de argumente și va returna produsul acesora.
Exemplu: task_3(1, 4, 5) ➞ 20
"""

# CODUL TĂU VINE MAI JOS:
def task_3(*args):
    result = 1
    for arg in args:
        result *= arg
    return result
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_3(task_3))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_4` care primește un număr arbitrar de perechi cheie-valoare și returnează un string care conține toate cheile și valorile concatenate separate de un spațiu.
Exemplu: task_4(a=1, b=2, c=3) ➞ 'a 1 b 2 c 3'
"""

# CODUL TĂU VINE MAI JOS:
def task_4(**kwargs):
    return ' '.join([f"{key} {value}" for key, value in kwargs.items()])
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_4(task_4))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_5` care primește un număr variabil de argumente și returnează două liste separate.
Prima listă conține toate argumentele de tip întreg sortate în ordine crescătoare, iar a doua listă conține denumirea tuturor argumentelor keyword care sunt de tip string sortate în ordine alfabetică.
Exemplu: task_6(3, 1, 2, a=10, b=20) ➞ [1, 2, 3], []
Exemplu: task_6(3, 1, 2, a=10, b=20, c='a') ➞ [1, 2, 3], ['c']
Exemplu: task_6(3, 1, 2, a=10, b=20, c='a', d='b') ➞ [1, 2, 3], ['c', 'd']
"""

# CODUL TĂU VINE MAI JOS:
def task_5(*args, **kwargs):
    integers = sorted([arg for arg in args if isinstance(arg, int)])
    strings = sorted([key for key, value in kwargs.items() if isinstance(value, str)])
    return integers, strings
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_5(task_5))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_6` care primește un număr variabil de argumente și returnează un dicționar care conține toate argumentele keyword ca key și valoarea acestora ca value.
Exemplu: task_6(a=1, b=2, c=3) ➞ {'a': 1, 'b': 2, 'c': 3}
"""

# CODUL TĂU VINE MAI JOS:
def task_6(**kwargs):
    return kwargs
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_6(task_6))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_7` care poate primi un număr nedeterminat de argumente atât string-uri cât și numere și va returna un dicționar cu două chei: `str` și `int`.
Cheia `str` va avea o listă cu toate string-urile primite ca argumente, iar cheia `int` va avea o listă cu toate numerele primite ca argumente.
Exemplu: task_7(1, 'a', 2, 'b') ➞ {'str': ['a', 'b'], 'int': [1, 2]}
"""

# CODUL TĂU VINE MAI JOS:
def task_7(*args):
    str_list = [arg for arg in args if isinstance(arg, str)]
    int_list = [arg for arg in args if isinstance(arg, int)]
    return {'str': str_list, 'int': int_list}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_7(task_7))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_8` care primește un număr variabil de argumente și returnează un dicționar cu două chei: `palindrom` și `non_palindrom`.
Cheia `palindrom` va avea o listă cu toate argumentele care sunt palindroame, iar cheia `non_palindrom` va avea o listă cu toate argumentele care nu sunt palindroame.
Exemplu: task_8('madam', 'hello', 'level', 'world') ➞ {'palindrom': ['madam', 'level'], 'non_palindrom': ['hello', 'world']}
"""

# CODUL TĂU VINE MAI JOS:
def task_8(*args):
    palindromes = [arg for arg in args if str(arg) == str(arg)[::-1]]
    non_palindromes = [arg for arg in args if str(arg) != str(arg)[::-1]]
    return {'palindrom': palindromes, 'non_palindrom': non_palindromes}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_8(task_8))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_9` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
Funcția va returna toate argumentele care sunt multipli ai lui `number`.
Exemplu: task_9(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
"""

# CODUL TĂU VINE MAI JOS:
def task_9(*args, number):
    return [arg for arg in args if arg % number == 0]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_9(task_9))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_10` care primește un număr variabil de argumente de tip integer și un argument `number` de tip integer.
Funcția va returna toate argumentele care sunt divizibile cu `number`.
Exemplu: task_10(1, 2, 3, 4, 5, number=2) ➞ [2, 4]
"""

# CODUL TĂU VINE MAI JOS:
def task_10(number, *args):
    return [num for num in args if num % number == 0]
print(task_10(2, 1, 2, 3, 4, 5))  # Output: [2, 4]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_10(task_10))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_11` care primește un număr variabil de argumente de tip integer care reprezintă șirul Fibonacci.
Funcția va returna valoarea True dacă șirul Fibonacci este corect și False în caz contrar.
Exemplu: task_11(1, 1, 2, 3, 5, 8) ➞ True
Exemplu: task_11(1, 1, 2, 3, 5, 9) ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_11(*args):
    if len(args) < 2:
        return False

    a, b = args[:2]
    for num in args[2:]:
        if num != a + b:
            return False
        a, b = b, num
    return True
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_11(task_11))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_12` care primește un număr variabil de argumente de tip integer.
Funcția va returna True dacă toate argumentele sunt numere prime și False în caz contrar.
Exemplu: task_12(2, 3, 5, 7) ➞ True
Exemplu: task_12(1, 2, 3, 4) ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def task_12(*args):
    return all(is_prime(num) for num in args)
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_12(task_12))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_13` care primește obligatoriu un argument de tip string și un număr variabil de argumente de tip string.
Funcția va returna True dacă toate argumentele sunt anagrame și False în caz contrar.
Exemplu: task_13('listen', 'silent') ➞ True
Exemplu: task_13('hello', 'world') ➞ False
"""

# CODUL TĂU VINE MAI JOS:
def task_13(word, *args):
    return all(sorted(word) == sorted(arg) for arg in args)

# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_13(task_13))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_14` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
Funcția va returna o listă cu toate argumentele care conțin `sub_string`.
Exemplu: task_14('home', 'same', 'meme', sub_string="me") ➞ ['home', 'meme', 'same']
"""

# CODUL TĂU VINE MAI JOS:
def task_14(sub_string, *args):
    return [arg for arg in args if sub_string in arg]
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_14(task_14))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_15` care primește un argument `sub_string` de tip string și un număr variabil de argumente de tip string.
Funcția va returna un dicționar cu două chei: `contains` și `not_contains`.
Cheia `contains` va avea o listă cu toate argumentele care conțin `sub_string`, iar cheia `not_contains` va avea o listă cu toate argumentele care nu conțin `sub_string`.
Exemplu: task_15('home', 'same', 'meme', sub_string = 'me') ➞ {'contains': ['home', 'same', 'meme'], 'not_contains': []}
"""

# CODUL TĂU VINE MAI JOS:
def task_15(sub_string, *args):
    contains_substring = [arg for arg in args if sub_string in arg]
    not_contains_substring = [arg for arg in args if sub_string not in arg]
    return {'contains': contains_substring, 'not_contains': not_contains_substring}
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_15(task_15))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_16` care va primi un număr variabil de argumente de tip integer și un argument `ooperation` de tip string.
Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor.
Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
Exemplu: task_16(2, 3, 4, 5, operation='add') ➞ 14
Exemplu: task_16(2, 3, 4, 5, operation='sub') ➞ -10
Exemplu: task_16(2, 3, 4, 5, operation='mul') ➞ 120
Exemplu: task_16(2, 3, 4, 5, operation='div') ➞ 0.008333333333333333
"""

# CODUL TĂU VINE MAI JOS:
def task_16(*args, operation='add'):
    if operation == 'add':
        return sum(args)
    elif operation == 'sub':
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif operation == 'mul':
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == 'div':
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    else:
        return "Invalid operation"
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_16(task_16))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_17` care primește un argument `number` după putea primi diferite argumente keyword precum `add`, `sub`, `mul`, `div` care vor fi liste cu numere.
Funcția va returna rezultatul operației specificate de argumentul `operation` aplicată tuturor argumentelor. Mai multe operații pot fi aplicate. Ordinea operațiilor va fi în ordinea în care sunt specificate.
Operațiile posibile sunt: `add`, `sub`, `mul`, `div`.
Exemplu: task_17(2, add=[3, 4, 5]) ➞ 14
Exemplu: task_17(2, sub=[3, 4, 5]) ➞ -10
Exemplu: task_17(2, mul=[3, 4, 5]) ➞ 120
Exemplu: task_17(2, div=[3, 4, 5]) ➞ 0.008333333333333333
Exemplu: task_17(2, add=[3, 4, 5], sub=[1, 2]) ➞ 11
"""

# CODUL TĂU VINE MAI JOS:
def task_17(number, **kwargs):
    result = number
    for operation, values in kwargs.items():
        if operation == 'add':
            result += sum(values)
        elif operation == 'sub':
            result -= sum(values)
        elif operation == 'mul':
            for value in values:
                result *= value
        elif operation == 'div':
            for value in values:
                result /= value
    return result
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_17(task_17))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_18` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi caracterele întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale caracterelor.
Exemplu: task_18('hello', 'world') ➞ {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_18(*args):
    char_count = {}
    for arg in args:
        for char in arg:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_18(task_18))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_19` care primește un număr variabil de argumente de tip integer și va returna un dicționar în care cheile vor fi numerele prime întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale numerelor prime.
Exemplu: task_19(1, 2, 3, 4, 5, 6, 7, 8, 9) ➞ {2: 1, 3: 1, 5: 1, 7: 1}
"""

# CODUL TĂU VINE MAI JOS:
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def task_19(*args):
    prime_counts = {}
    for num in args:
        if is_prime(num):
            if num in prime_counts:
                prime_counts[num] += 1
            else:
                prime_counts[num] = 1
    return prime_counts
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_19(task_19))
# VERIFICATION PROCESS

"""
Task: Creați o funcție cu numele `task_20` care primește un număr variabil de argumente de tip string și va returna un dicționar în care cheile vor fi lungimile cuvintelor întâlnite în argumentele primite, iar valorile vor fi numărul de apariții ale lungimilor cuvintelor.
Exemplu: task_20('hello', 'world') ➞ {5: 2}
Exemplu: task_20('hello', 'world', 'python') ➞ {5: 2, 6: 1}
"""

# CODUL TĂU VINE MAI JOS:
def task_20(*args):
    word_length_count = {}
    for arg in args:
        if len(arg) in word_length_count:
            word_length_count[len(arg)] += 1
        else:
            word_length_count[len(arg)] = 1
    return word_length_count
# CODUL TĂU VINE MAI SUS:

# VERIFICATION PROCESS
print(session.check_task_20(task_20))
print(session.get_completion_percentage())
# VERIFICATION PROCESS
#Tema p-u acasă (TPA) a fost realizată de Maxim Papanaga :D
