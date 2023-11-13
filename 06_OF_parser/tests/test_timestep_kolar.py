# %%
from OFParser.timestep import TimeStep
# %%

# Time counter tests

def test_time_existence() -> None:
    T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
    T.Time

def test_time_type() -> None:
    T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
    assert type(T.Time) == float

def test_time_noneg() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(Time=-1.0,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)

def test_time_nonzero() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(Time=0.0,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)

# Particle mass tests

def test_mass_existence() -> None:
    T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
    T.Current_mass_in_system

def test_mass_type() -> None:
    T = TimeStep(Time=-1.0,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
    assert type(T.Current_mass_in_system) == float

def test_mass_noneg() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=-4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=-1.0)

def test_mass_toenergy():
    with pytest.raises(AssertionError):
        T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=5.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)

# %%
