# Aceasta este a doua ta sarcină legată a leciei legate de stringuri în python

# Creează o variabilă numită `name` și seteaz-o la numele tău

# CODUL TĂU VINE MAI JOS:
name = "Max"
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `name` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(name)
# CODUL TĂU VINE MAI SUS:

# Acum creează o nouă variabilă numită `name2` și seteaz-o la valoarea variabilei `name` și afișează valoarea variabilei `name2` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
name = "Alex"
name2 = name
print(name2)
# CODUL TĂU VINE MAI SUS:

# Acum printează ultimul caracter al variabilei `name` folosind indexarea

# CODUL TĂU VINE MAI JOS:
last_character = name[-1]
print(last_character)
# CODUL TĂU VINE MAI SUS:

# Acum printează primele 3 caractere ale variabilei `name` folosind slicing

# CODUL TĂU VINE MAI JOS:
first_three_characters = name[:3]
print(first_three_characters)
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în majuscule folosind metoda `upper`

# CODUL TĂU VINE MAI JOS:
uppercase_name = name.upper()
print(uppercase_name)
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în minuscule folosind metoda `lower`

# CODUL TĂU VINE MAI JOS:
lowercase_name = name.lower()
print(lowercase_name)
# CODUL TĂU VINE MAI SUS:

# Acum printează concatenarea variabilelor `name` și `name2`

# CODUL TĂU VINE MAI JOS:
concatenated_names = name + name2
print(concatenated_names)
# CODUL TĂU VINE MAI SUS:

# Creează o variabilă `text` și setează-i un text la alegere, cu restricția ca acesta să conțină mai multe rânduri

# CODUL TĂU VINE MAI JOS:
text = """Bla bla bla foarte mult text
anevoios si fara sens pentru
a indepleni sarcina pentru
acasa de programare python."""
# CODUL TĂU VINE MAI SUS:

# Verifică dacă variabila `text` conține cuvântul `python`

# CODUL TĂU VINE MAI JOS:
if 'python' in text:
    print("Yes")
else:
    print("No")
# CODUL TĂU VINE MAI SUS:

# Folosește metoda replace pentru a înlocui litera `a` din variabila `text` cu litera `e`

# CODUL TĂU VINE MAI JOS:
modified_text = text.replace('a', 'e')
print(modified_text)
# CODUL TĂU VINE MAI SUS:

# Folosește metoda split pentru a transforma variabila `text` într-o listă de cuvinte

# CODUL TĂU VINE MAI JOS:
word_list = text.split()
print(word_list)
# CODUL TĂU VINE MAI SUS:

# Creează un f-string care să conțină variabilele `name` și `name2`

# CODUL TĂU VINE MAI JOS:
name = "Max"
name2 = "Mili"

f_string = f"My name is {name} and her name is {name2}!"
print(f_string)
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat se termină cu `!`

# CODUL TĂU VINE MAI JOS:
if f_string.endswith('!'):
    print("Yes")
else:
    print("No")
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat începe cu `Hello`

# CODUL TĂU VINE MAI JOS:
if f_string.startswith('Hello'):
    print("Yes")
else:
    print("No")
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `!` în string-ul creat

# CODUL TĂU VINE MAI JOS:
index1 = f_string.index('!')
print("Semnul de exclamare: ", index1)
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `o` în string-ul creat folosind altă metodă

# CODUL TĂU VINE MAI JOS:
index2 = f_string.find('0')
print("Litera 'O': ", index2)
# CODUL TĂU VINE MAI SUS:

# Utilizând format string-uri, creează un string care să conțină variabilele `name` și `name2`

# CODUL TĂU VINE MAI JOS:
name = "Max"
name2 = "Mili"

f_string = f"My name is {name} and her name is {name2}!"
# CODUL TĂU VINE MAI SUS:

# Concatenează string-ul creat cu string-ul `text`

# CODUL TĂU VINE MAI JOS:
joined_text = f_string + text
print(joined_text)
# CODUL TĂU VINE MAI SUS:

# Afișează lungimea string-ului creat

# CODUL TĂU VINE MAI JOS:
print("Lungimea:", len(joined_text))
# CODUL TĂU VINE MAI SUS:

# Aceasta a fost tot pentru această sarcină
#Tema p-u acasă (TPA) a fost realizată de Maxim Papanaga :D
