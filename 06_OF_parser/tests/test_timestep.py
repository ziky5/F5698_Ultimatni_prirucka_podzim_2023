from OFParser.timestep import TimeStep

def test() -> None:
    pass


# Time counter and system mass tests

from OFParser.timestep import TimeStep
import pytest

# Time counter tests

def test_time_existence() -> None:
    T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
    T.Time

def test_time_type() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(Time="1",Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
    with pytest.raises(AssertionError):
        T = TimeStep(Time=10,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
    with pytest.raises(AssertionError):
        T = TimeStep(Time=[1.0],Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)

def test_time_noneg() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(Time=-1.0,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)

def test_time_nonzero() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(Time=0.0,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)

# System mass tests

def test_mass_existence() -> None:
    T = TimeStep(Time=-1.0,Current_number_of_parcels=10,Current_mass_in_system=4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
    T.Current_mass_in_system

def test_mass_type() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system="4.5",Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
    with pytest.raises(AssertionError):
        T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=4,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
    with pytest.raises(AssertionError):
        T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=[4.5],Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)

def test_mass_noneg() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=-4.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=-1.0)

def test_mass_toenergy():
    with pytest.raises(AssertionError):
        T = TimeStep(Time=1.0,Current_number_of_parcels=10,Current_mass_in_system=55.5,Linear_momentum=(2.0,2.0,1.0),Abs_Linear_momentum=3.0,Linear_kinetic_energy=1.0)
# Calculating energy as  E = (P^2)/(2M)  , where P=Abs_Linear_momentum and M=Current_mass_in_system.        

# End of Time counter and system mass tests
