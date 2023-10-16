# print(100//33)
# print(100/33)
# print(100%33)
# Kontrolni balik k dataclass
#SADOVSKY .. SNAHA BYLA .. BOHUZEL VIZ KOMENTARE NIZE .. MANIPULACE NEFUNGUJE Z TEXTU JAK JSEM OCEKAVAL.. 60 MINUT JE OUT.. JE TO NA VAS .. GOOD LUCK
from dataclasses import dataclass, field
from typing import List

# Definice datové třídy KinematicCloud s atributy pro jednotlivé části odstavce
@dataclass
class KinematicCloud:
    parcels: int = field(default=None)  # Počet parcel
    mass: float = field(default=None)    # Aktuální hmotnost v systému
    momentum: List[float] = field(default_factory=list)  # Lineární moment (x, y, z)
    linear_momentum: float = field(default=None)  # Velikost lineárního momentu
    kinetic_energy: float = field(default=None)   # Lineární kinetická energie
    model1: dict = field(default_factory=dict)      # Údaje pro model1 (klíčová slova)
    parcel_fate: dict = field(default_factory=dict)  # Údaje o osudu parcel

    # Metoda pro vytvoření instance KinematicCloud z textového vstupu
    @classmethod
    def from_text(cls, text):
        data = {}  # Slovník pro ukládání extrahovaných údajů
        model1 = {}  # Slovník pro údaje o model1
        parcel_fate = {}  # Slovník pro údaje o osudu parcel

        lines = text.split('\n')  # Rozdělení textu na řádky

        for line in lines:
            # Hledáme klíčová slova v jednotlivých řádcích
            if "Current number of parcels" in line:
                data["parcels"] = int(line.split('=')[-1].strip())
            elif "Current mass in system" in line:
                data["mass"] = float(line.split('=')[-1].strip())
            elif "Linear momentum" in line:
                # Extrahujeme komponenty lineárního momentu (x, y, z)
                components = line.split('=')[-1].strip()
                components = components.replace('(', '').replace(')', '')  # Odebrání závorek
                components = components.split()
                components = [float(x) for x in components]
                data["momentum"] = components
            elif "|Linear momentum|" in line:
                data["linear_momentum"] = float(line.split('=')[-1].strip())
            elif "Linear kinetic energy" in line:
                data["kinetic_energy"] = float(line.split('=')[-1].strip())
            elif "model1:" in line:
                # Načítáme údaje pro model1 až do dalšího klíčového slova
                while True:
                    line = lines.pop(0)
                    if not line.strip():
                        continue
                    if line.strip().startswith('-'):
                        # Údaje o osudu parcel, ukládáme do model1
                        components = line.split('=')
                        key = components[0].strip()
                        value = float(components[1].strip().split(',')[0])
                        model1[key] = value
                    else:
                        # Konec model1
                        break
                data["model1"] = model1
            elif "Parcel fate (number, mass)" in line:
                # Načítáme údaje o osudu parcel
                while True:
                    line = lines.pop(0)
                    if not line.strip():
                        continue
                    if line.strip().startswith('-'):
                        components = line.split('=')
                        key = components[0].strip()
                        value = float(components[1].strip().split(',')[0])
                        parcel_fate[key] = value
                    else:
                        # Konec údajů o osudu parcel
                        break
                data["parcel_fate"] = parcel_fate

        # Vytvoření instance KinematicCloud s extrahovanými údaji
        return cls(**data)

# Textový vstup reprezentující odstavce

text = '''
Kontrolni balik k dataclass
#
Solving 3-D cloud kinematicCloud
Cloud: kinematicCloud
    Current number of parcels       = 497200
    Current mass in system          = 3.30057995e-20
    Linear momentum                 = (1.3883565e-21 7.71079581e-21 -8.75499278e-18)
   |Linear momentum|                = 8.75499629e-18
    Linear kinetic energy           = 1.92456112e-15
    model1:
        number of parcels added     = 500000
        mass introduced             = 3.31916729e-20
    Parcel fate (number, mass)      : patch .*
      - escape                      = 2800, 1.85873368e-22
      - stick                       = 0, 0
cloud.linear_momentum = -99...................................#tady to krmim ... snizi pocet radku ale hlaska je blbe, kdyz dam 5

ExecutionTime = 644.39 s  ClockTime = 645 s

Time = 5.000e-07

Evolving kinematicCloud
'''

# Tento text obsahuje všechny klíčové informace, které kód očekává, včetně počtu parcel, hmotnosti, 
# lineárního momentu a dalších atributů. Zkopírujte tento text do  kódu nebo vytvořte podobný vstupní text pro další odstavce.
# Ujisti se, že vstupní text pro všechny odstavce obsahuje tyto základní informace, abys mohl úspěšně vytvořit instance KinematicCloud.
# S tímto textem by neměly být problémy .. ale sakra jsou ... kód by měl provádět analýzu a manipulaci dat, jak bylo zamýšleno, bez zobrazování "Chybějící údaje v textu pro tento odstavec."
# Ujisti  se... to tam .. ale stejne to nejde, že textový vstup obsahuje všechny potřebné údaje ve správném formátu, aby mohl být vytvořen instanci KinematicCloud bez problémů.


# Rozdělení textu na odstavce (každý odstavec je jeden prvek v seznamu)
paragraphs = text.split('\n\n')

# # Rozdělení textu na odstavce (každý odstavec je jeden prvek v seznamu)
# paragraphs = text.split('\n\n')

# Pro každý odstavec vytvoříme instanci KinematicCloud
for paragraph in paragraphs:
    cloud = KinematicCloud.from_text(paragraph)
    # Kontrola, zda byly v textu dostupné potřebné údaje
    if cloud.parcels is not None and cloud.linear_momentum is not None:
        # Provádíme analýzu a manipulaci pouze pokud jsou dostupné potřebné údaje
        if cloud.linear_momentum > 1e-17:
            print("Velikost lineárního momentu je větší než 1e-17.")
            # Manipulace s daty:
            # Zde můžete provádět další manipulace s daty v instanci "cloud"
        else:
            print("Velikost lineárního momentu je nižší nebo rovna 1e-17.")
    else:
        print("Chybějící údaje v textu pro tento odstavec.")



###Pokusnej text... ale ani ten nejde

# text = '''
# Kontrolni balik k dataclass
# #
# Solving 3-D cloud kinematicCloud
# Cloud: kinematicCloud
#     Current number of parcels       = 497200
#     Current mass in system          = 3.30057995e-20
#     Linear momentum                 = (1.3883565e-21 7.71079581e-21 -8.75499278e-18)
#    |Linear momentum|                = 8.75499629e-18
#     Linear kinetic energy           = 1.92456112e-15
#     model1:
#         number of parcels added     = 500000
#         mass introduced             = 3.31916729e-20
#     Parcel fate (number, mass)      : patch .*
#       - escape                      = 2800, 1.85873368e-22
#       - stick                       = 0, 0

# ExecutionTime = 644.39 s  ClockTime = 645 s

# Time = 5.000e-07

# Evolving kinematicCloud
# '''
