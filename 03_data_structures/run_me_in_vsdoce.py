# %%
# Začneme definicí prázdné třídy, která bude (za nedlouho) reprezentovat
# data, které budeme chtít zparsovat z logu, pro každý časový
# krok.


class TimeRecord:
    def __init__(self) -> None:
        pass


# Vedeme poměrně rozsáhlou diskusi, co je to konstruktor
# (metoda __init__) a co je argument self a proč ho
# nidky explicitně nepředáváme do metod, které voláme na
# objektech.
#
# Zamýšlíme se i nad tím, co znamená ona šipka (vscode nám to
# automaticky doplnil) u definice kostruktoru ("-> None").
# Jedná se tzv. anotaci, která v tomto případě říká,
# že konstruktor vrací None (to je způsob, kterým v Pythonu,
# říkáme, že metoda či funkce nevrací nic).

# %%
# Konstruktor se volá pomocí jména třídy a operátoru
# kulatých závorek. Zde vytváříme objekt, který pojmenujeme
# "tr" a který je třídy "TimeRecord".

tr = TimeRecord()
tr


# %%
# TimeRecord toho moc neumí, a tak se věnujeme definici další třídy
# která by mohla být základem pro budoucí reálné použití. Oblasti,
# které jsme zběžně pokryli:
#
# 1. Povinné a nepoviné (key-word) argumenty konstruktoru (resp. metod obecně)
# 2. Použití self reference na objekt.
# 3. Assert statement.
# 4. f-strigy
# 5. Definice další (opět speciální) metody __repr__
# 6. Anotace u argumentů a použití nástroje mypy.
# 7. Definice statické metody.
# 8. Zlehka a velice opatrně jsme diskutovali dědění tříd.


class TimeRecord2:
    def __init__(self, time: float, current_number_of_parcels: int = -1) -> None:
        assert (
            current_number_of_parcels >= 0
        ), f"Current number of parcels has to be greater then zero (it is: {current_number_of_parcels})"
        self.time = time
        self.current_number_of_parcels = current_number_of_parcels

    def __repr__(self) -> str:
        return f"TimeRecord2({self.time}, {self.current_number_of_parcels})"

    @staticmethod
    def static():
        print("nevim")


# %%

tr2 = TimeRecord2(0.01, current_number_of_parcels=50000)
tr2

# %%
tr2.time, tr2.current_number_of_parcels

# %%
