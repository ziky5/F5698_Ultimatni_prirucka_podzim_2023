# Martin
# Timestep
# existuje casovy krok?
# jde o float?
# je nezaporny?

# parcel mass
# existuje?
# jde o float?
# je nezaporny?

# Samuel
# Current number of parcels
# existuje?
# zparsujeme "log_example", je "Current number of parcels" rovny 6380 ?
# jde o int?
# je nezaporny?

# Current mass in system
# existuje?
# zparsujeme "log_example", je "Current number of parcels" rovny 6380 ?
# jde o float?
# je nezaporny?
# "Current number of parcels" * 6.63352599e-26 je rovna "Current mass in system" - aproximate

# Tomas
# Linear momentum
# jde vektor? tuple, sequence
# ma tri cisla?
# jsou cisla float?
# existuje

# |Linear momentum|
# existuje?
# zparsujeme "log_example", je "Current number of parcels" rovny 6380 ?
# jde o float?
# je nezaporny?
# odpovida velikosti "Linear momentum"

# Linear kinetic energy
# existuje?
# zparsujeme "log_example", je "Current number of parcels" rovny 6380 ?
# jde o float?
# je nezaporny?
# odpovida energie velikosti momentu hybnosti

# read(path)
# path -> cesta k souboru, ktery obsahuje vypis jednoho caseveho kroku, soubor zparsuje a vytvori dataclass s danymi parametry
# test 1 - zparsuje a zkusi vytvorit dataclass
# test 2 - zparsuje, vytvori dataclassu a porovna repr s nejakym ocekavanym