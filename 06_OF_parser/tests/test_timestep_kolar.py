# %%
from OFParser.timestep import TimeStep
# %%

# Time counter tests

def test_time_existence() -> None:
    T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=10.0,Linear_momentum=(5.0,4.0,3.0),Abs_Linear_momentum=1.0,Linear_kinetic_energy=x )
    T.Time

def test_time_type() -> None:
    assert type(T.Time) == float

def test_time_noneg() -> None:
    time_noneg = float(abs(T.Time))
    assert time_noneg == T.Time

# Particle mass tests

def test_mass_existence() -> None:
    T.Current_mass_in_system

def test_mass_type() -> None:
    assert type(T.Current_mass_in_system) == float

def test_mass_noneg() -> None:
    mass_noneg = float(abs(T.Current_mass_in_system))
    assert mass_noneg == T.Current_mass_in_system








