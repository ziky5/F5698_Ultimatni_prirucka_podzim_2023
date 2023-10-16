# Uzitecne odkazy
# https://peps.python.org/pep-0557/
# https://docs.python.org/3/library/dataclasses.html
# %%
from dataclasses import dataclass, field
import numpy as np
# %%
# ukazka definice dataclassy a jak se pomoci ni da nadefinovat class z minule hodiny
# diskuze i výhodách dataclass

@dataclass
class TimeRecord3():
    time: float
    current_number_of_parcels: int = -1

    def print_time(self):
        print(f'Time: {self.time}')
# %%
a = TimeRecord3(0.01, current_number_of_parcels=50000)
print(a)
# %%
# ukázka stejné dataclassy, ale s tim rozdilem, že obsahuje parametr definovaný skrz field deskriptor
# v něm jsem řekl aby nebyl zahrnut v repru, nadefinoval jeho defaultni hodnotu a rekl ze musi byt "kw_only"
# proběhla diskuze o všech těchto možnostech a také možnosti definovat hodnoty pomocí default_factory

@dataclass
class TimeRecord4():
    time: float
    a: int = field(repr=False, default = 3, kw_only=True)
    current_number_of_parcels: int = -1

    def print_time(self):
        print(f'Time: {self.time}')
# %%
b = TimeRecord4(0.01, a = 5, current_number_of_parcels=50000)
print(b)
# %%
# ukázka chování "kw_only" vůči pořádí argumentů
b = TimeRecord4(0.01, 50000, a = 5)
print(b)
# %%
# ukázka dataclassy kde jeden z parametrů není zahrnut v "__init__" funkci, ale je zahrnutá v "__post_init__"
# diskuze o isinstance funkci a typech, možnost předefinování chování funknce vůči operátoru "==" (compare argument funkce field)

@dataclass
class triangle():
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        assert isinstance(self.a, float), 'Parameter "a" has to be float'
        assert isinstance(self.b, float), 'Parameter "b" has to be float'

        self.c = np.sqrt(self.a*self.a + self.b*self.b)

# %%
test = triangle(3.0,4.0)
# %%
test
# %%
