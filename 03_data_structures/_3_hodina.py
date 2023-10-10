# Sadovsky Martin COMMIT

print("hallo world")

######################################################################################

""" Objektově orientované programování

Třída - definice
Třída se vytvoří pomocí klíčového slova class .
Třída (s poli a metodami) je tvořena blokem kódu, proto by mělo být použito odsazení.
__init__ (self) je speciální metoda (funkce) volaná pokaždé, když vytvoříme objekt založený na dané třídě.
Metoda __init__ se nazývá konstruktor.
Parametr self je prvním nezbytným parametrem v metodách. Při použití mohou metody odkazovat na
objekt, na který jsou volány. """

Třída - definice
class Animal:
    NAME = "" # class variable
    AGE = 0 # class variable
    def __init__(self):
        self.name = "John" # set the default value for the name field of the
Animal class object self.age = 2
    def print_details(self): # method for printing the state of an object
        print(f"Name: {self.name}, age: {self.age}.")


""" Vytvoření objektu
Objekt lze vytvořit až po definování třídy.
Metoda __init__ vytvoří objekt.
Chcete-li se dostat k hodnotě pole nebo provést metodu na objektu, použijte operátor tečky . . """


class Animal:
...

""" Nezávislost objektů
Každý objekt má svůj vlastní stav. Změnou hodnot polí jednoho objektu neovlivníme stejná pole jiných objektů. """

class Animal:
    ...
puppy = Animal()
dog = Animal() # Creates a second Animal class object
puppy.age = 1
puppy.name = "Rex Junior"
dog.age = 10
dog.name = "Rex Senior"
print(f"My dog: {puppy.name}, {puppy.age} and the older dog: {dog.name},
{dog.age}")

""" Konstruktor __init__
Namísto nastavení výchozích hodnot pro pole objektů je můžeme předat konstruktoru při vytváření objektu. """

class Animal:
def __init__(self, name="Rex", age=2):
self.name = name
self.age = age























