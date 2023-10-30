# Martinův první pokus o nějaký code ve VScodu
# ...výsledek hodinového snažení -- snad bylo vše dobře pochopeno :-) jde o daleko osekanější řešení, než tomu je u kolegy Sadovského..

# Struktura souboru dat:
# -----------------------------------------------------------------------------------
#
# Time = 1.000e-07
#
# Evolving kinematicCloud
#
# Solving 3-D cloud kinematicCloud
#
# Cloud: kinematicCloud injector: model1
#    Added 500000 new parcels
#
# Cloud: kinematicCloud
#    Current number of parcels       = 500000
#    Current mass in system          = 3.31916729e-20
#    Linear momentum                 = (1.31194295e-21 5.68025011e-21 -9.63186281e-18)
#   |Linear momentum|                = 9.63186458e-18
#    Linear kinetic energy           = 1.61448549e-15
#    model1:
#        number of parcels added     = 500000
#        mass introduced             = 3.31916729e-20
#    Parcel fate (number, mass)      : patch .*
#      - escape                      = 0, 0
#      - stick                       = 0, 0
#
# ExecutionTime = 641.05 s  ClockTime = 642 s
#
# -----------------------------------------------------------------------------------
# %%
# Import

from dataclasses import dataclass
# %%
# Definuji balík dat pro jednotlivé záznamy

@dataclass
class Data():
    time: float    # Time
    count: int     # Particle counter ("Current number of parcels")
    mass: float    # Mass ("Current mass in system")
    mmt: float     # Linear momentum
    absmmt: float  # Abs of linear momentum
    en: float      # Energy ("Linear kinetic energy")
    extime: float  # Execution time

# Nějaké chybové hlášky, aby bylo jasno...

    def __post_init__(self):
        assert isinstance(self.time, float), "Data type of -time- has to be -float-"
        assert isinstance(self.count, int), "Data type of -count- has to be -int-"
        assert isinstance(self.mass, float), "Data type of -mass- has to be -float-"
        assert isinstance(self.mmt, float), "Data type of -mmt- has to be -float-"
        assert isinstance(self.absmmt, float), "Data type of -absmmt- has to be -float-"
        assert isinstance(self.en, float), "Data type of -en- has to be -float-"
        assert isinstance(self.extime, float), "Data type of -extime- has to be -float-"

# A teď definuji různé užitečné printovací operace,
# asi se to pak může přepsat (z "printu") na vytažení informace do nějakého dalšího datového souboru

    def gettime(self):
        print(f"Time: {self.time} /", f"Execution time: {self.extime}")
    def getstatus(self):
        print(f"Time: {self.time} /", f"Particles: {self.count}")
    def getsystem(self):
        print(f"Time: {self.time} /", f"Mass: {self.mass} /", f"Momentum: {self.mmt} /", f"Kinetic energy: {self.en}")
# %%
#
#
#
# Následují jen nějaké pokusy, jestli všechno dobře funguje
#
#
#
# %%
a = Data(time = 20.15, count = 50000, mass = 2.0, mmt = 865.0, absmmt = 865.0, en = 300.0, extime = 0.0001)
# %%
Data.gettime(a)
Data.getstatus(a)
Data.getsystem(a)
# %%
# Error
b = Data(time = 20.15, count = 50000.15, mass = 2.0, mmt = 865.0, absmmt = 865.0, en = 300.0, extime = 0.0001)
# %%
# Konec :-)