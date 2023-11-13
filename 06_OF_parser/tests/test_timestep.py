from OFParser.timestep import TimeStep

DATA = """\
Time = 8.190e-05

Evolving kinematicCloud

Solving 3-D cloud kinematicCloud
Cloud: kinematicCloud
    Current number of parcels       = 6380
    Current mass in system          = 4.23525746e-22
    Linear momentum                 = (-1.44664513e-21 -1.94003635e-21 -5.42703062e-20)
   |Linear momentum|                = 5.43242364e-20
    Linear kinetic energy           = 2.41789442e-16
    model1:
        number of parcels added     = 500000
        mass introduced             = 3.31916729e-20
    Parcel fate (number, mass)      : patch .*
      - escape                      = 493620, 3.27681468e-20
      - stick                       = 0, 0
"""


def test() -> None:
    pass


# Time counter and system mass tests

from OFParser.timestep import TimeStep
import pytest

# Time counter tests


def test_time_existence() -> None:
    T = TimeStep(
        Time=1.0,
        Current_number_of_parcels=10,
        Current_mass_in_system=4.5,
        Linear_momentum=(2.0, 2.0, 1.0),
        Abs_Linear_momentum=3.0,
        Linear_kinetic_energy=1.0,
    )
    T.Time


def test_time_type() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(
            Time="1",
            Current_number_of_parcels=10,
            Current_mass_in_system=4.5,
            Linear_momentum=(2.0, 2.0, 1.0),
            Abs_Linear_momentum=3.0,
            Linear_kinetic_energy=1.0,
        )
    with pytest.raises(AssertionError):
        T = TimeStep(
            Time=10,
            Current_number_of_parcels=10,
            Current_mass_in_system=4.5,
            Linear_momentum=(2.0, 2.0, 1.0),
            Abs_Linear_momentum=3.0,
            Linear_kinetic_energy=1.0,
        )
    with pytest.raises(AssertionError):
        T = TimeStep(
            Time=[1.0],
            Current_number_of_parcels=10,
            Current_mass_in_system=4.5,
            Linear_momentum=(2.0, 2.0, 1.0),
            Abs_Linear_momentum=3.0,
            Linear_kinetic_energy=1.0,
        )


def test_time_noneg() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(
            Time=-1.0,
            Current_number_of_parcels=10,
            Current_mass_in_system=4.5,
            Linear_momentum=(2.0, 2.0, 1.0),
            Abs_Linear_momentum=3.0,
            Linear_kinetic_energy=1.0,
        )


def test_time_nonzero() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(
            Time=0.0,
            Current_number_of_parcels=10,
            Current_mass_in_system=4.5,
            Linear_momentum=(2.0, 2.0, 1.0),
            Abs_Linear_momentum=3.0,
            Linear_kinetic_energy=1.0,
        )


# System mass tests


def test_mass_existence() -> None:
    T = TimeStep(
        Time=-1.0,
        Current_number_of_parcels=10,
        Current_mass_in_system=4.5,
        Linear_momentum=(2.0, 2.0, 1.0),
        Abs_Linear_momentum=3.0,
        Linear_kinetic_energy=1.0,
    )
    T.Current_mass_in_system


def test_mass_type() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(
            Time=1.0,
            Current_number_of_parcels=10,
            Current_mass_in_system="4.5",
            Linear_momentum=(2.0, 2.0, 1.0),
            Abs_Linear_momentum=3.0,
            Linear_kinetic_energy=1.0,
        )
    with pytest.raises(AssertionError):
        T = TimeStep(
            Time=1.0,
            Current_number_of_parcels=10,
            Current_mass_in_system=4,
            Linear_momentum=(2.0, 2.0, 1.0),
            Abs_Linear_momentum=3.0,
            Linear_kinetic_energy=1.0,
        )
    with pytest.raises(AssertionError):
        T = TimeStep(
            Time=1.0,
            Current_number_of_parcels=10,
            Current_mass_in_system=[4.5],
            Linear_momentum=(2.0, 2.0, 1.0),
            Abs_Linear_momentum=3.0,
            Linear_kinetic_energy=1.0,
        )


def test_mass_noneg() -> None:
    with pytest.raises(AssertionError):
        T = TimeStep(
            Time=1.0,
            Current_number_of_parcels=10,
            Current_mass_in_system=-4.5,
            Linear_momentum=(2.0, 2.0, 1.0),
            Abs_Linear_momentum=3.0,
            Linear_kinetic_energy=-1.0,
        )


def test_mass_toenergy():
    with pytest.raises(AssertionError):
        T = TimeStep(
            Time=1.0,
            Current_number_of_parcels=10,
            Current_mass_in_system=55.5,
            Linear_momentum=(2.0, 2.0, 1.0),
            Abs_Linear_momentum=3.0,
            Linear_kinetic_energy=1.0,
        )


# Calculating energy as  E = (P^2)/(2M)  , where P=Abs_Linear_momentum and M=Current_mass_in_system.

# End of Time counter and system mass tests


def test_from_str():
    ts = TimeStep.from_str(DATA)
    assert ts.Time == 8.190e-5
    assert ts.Current_number_of_parcels == 6380
    assert ts.Current_mass_in_system == 4.23525746e-22
    assert ts.Linear_momentum == (-1.44664513e-21, -1.94003635e-21, -5.42703062e-20)
    assert ts.Absolute_linear_momentum == 5.43242364e-20
    assert ts.Linear_kinetic_energy == 2.41789442e-16
    assert ts.models["model1"].number_of_parcels_added == 500000
    assert ts.models["model1"].mass_introduced == 3.31916729e-20
    assert ts.ParcelFate["escape"] == (493620, 3.27681468e-20)
    assert ts.ParcelFate["stick"] == (0, 0)


def test_current_number_of_parcels_exists():
    with pytest.raises(TypeError):
        timestep = TimeStep(time=1.0e-7,
                            # current_number_of_parcels=10,
                            current_mass_in_system=10.0,
                            linear_momentum=(5.0,4.0,3.0),
                            absolute_linear_momentum=1.0,
                            linear_kinetic_energy=1.61448549e-15,
                            number_of_parcels_added=500000,
                            mass_introduced=3.31916729e-20)
        
def test_current_number_of_parcels_is_int():
    timestep = TimeStep(time=1.0e-7,
                        current_number_of_parcels=500000,
                        current_mass_in_system=10.0,
                        linear_momentum=(5.0,4.0,3.0),
                        absolute_linear_momentum=1.0,
                        linear_kinetic_energy=1.61448549e-15,
                        number_of_parcels_added=500000,
                        mass_introduced=3.31916729e-20)
    assert isinstance(timestep.current_number_of_parcels, int)

def test_current_number_of_parcels_is_not_string():
    with pytest.raises(AssertionError):
        timestep = TimeStep(time=1.0e-7,
                            current_number_of_parcels='500000',
                            current_mass_in_system=10.0,
                            linear_momentum=(5.0,4.0,3.0),
                            absolute_linear_momentum=1.0,
                            linear_kinetic_energy=1.61448549e-15,
                            number_of_parcels_added=500000,
                            mass_introduced=3.31916729e-20)

def test_current_number_of_parcels_is_not_float():
    with pytest.raises(AssertionError):
        timestep = TimeStep(time=1.0e-7,
                            current_number_of_parcels=500000.1,
                            current_mass_in_system=10.0,
                            linear_momentum=(5.0,4.0,3.0),
                            absolute_linear_momentum=1.0,
                            linear_kinetic_energy=1.61448549e-15,
                            number_of_parcels_added=500000,
                            mass_introduced=3.31916729e-20)

def test_current_number_of_parcels_is_not_tuple():
    with pytest.raises(AssertionError):
        timestep = TimeStep(time=1.0e-7,
                            current_number_of_parcels=(500000,1),
                            current_mass_in_system=10.0,
                            linear_momentum=(5.0,4.0,3.0),
                            absolute_linear_momentum=1.0,
                            linear_kinetic_energy=1.61448549e-15,
                            number_of_parcels_added=500000,
                            mass_introduced=3.31916729e-20)

def test_current_number_of_parcels_is_positive():
    with pytest.raises(AssertionError):
        timestep = TimeStep(time=1.0e-7,
                            current_number_of_parcels=-500000,
                            current_mass_in_system=10.0,
                            linear_momentum=(5.0,4.0,3.0),
                            absolute_linear_momentum=1.0,
                            linear_kinetic_energy=1.61448549e-15,
                            number_of_parcels_added=500000,
                            mass_introduced=3.31916729e-20)



def test_number_of_parcels_added_is_int():
    timestep = TimeStep(time=1.0e-7,
                        current_number_of_parcels=500000,
                        current_mass_in_system=10.0,
                        linear_momentum=(5.0,4.0,3.0),
                        absolute_linear_momentum=1.0,
                        linear_kinetic_energy=1.61448549e-15,
                        number_of_parcels_added=500000,
                        mass_introduced=3.31916729e-20)
    assert isinstance(timestep.number_of_parcels_added, int)

def test_number_of_parcels_added_is_not_string():
    with pytest.raises(AssertionError):
        timestep = TimeStep(time=1.0e-7,
                            current_number_of_parcels=500000,
                            current_mass_in_system=10.0,
                            linear_momentum=(5.0,4.0,3.0),
                            absolute_linear_momentum=1.0,
                            linear_kinetic_energy=1.61448549e-15,
                            number_of_parcels_added='500000',
                            mass_introduced=3.31916729e-20)

def test_number_of_parcels_added_is_positive():
    with pytest.raises(AssertionError):
        timestep = TimeStep(time=1.0e-7,
                            current_number_of_parcels=500000,
                            current_mass_in_system=10.0,
                            linear_momentum=(5.0,4.0,3.0),
                            absolute_linear_momentum=1.0,
                            linear_kinetic_energy=1.61448549e-15,
                            number_of_parcels_added=-500000,
                            mass_introduced=3.31916729e-20)

def test_number_of_parcels_added_is_leq_current_number_of_parcels():
    timestep = TimeStep(time=1.0e-7,
                        current_number_of_parcels=500000,
                        current_mass_in_system=10.0,
                        linear_momentum=(5.0,4.0,3.0),
                        absolute_linear_momentum=1.0,
                        linear_kinetic_energy=1.61448549e-15,
                        number_of_parcels_added=500000,
                        mass_introduced=3.31916729e-20)
    assert timestep.number_of_parcels_added <= timestep.current_number_of_parcels
    

class TestLinearMomentumClass():
    Linear_momentum = (-1.44664513e-21, -1.94003635e-21, -5.42703062e-20)

    def test_linear_momentum_exists(self) -> None:
        a = TimeStep(Linear_momentum = self.Linear_momentum, Time = 8.190e-05, Current_number_of_parcels = 6380,
                      Current_mass_in_system = 4.23525746e-22, Linear_kinetic_energy = 2.41789442e-16,
                      Absolute_linear_momentum = 5.43242364e-20)

    def test_linear_momentum_is_tuple() -> None:
        with pytest.raises(AssertionError):
            a = TimeStep(Linear_momentum = 5, Time = 8.190e-05, Current_number_of_parcels = 6380,
                      Current_mass_in_system = 4.23525746e-22, Linear_kinetic_energy = 2.41789442e-16,
                      Absolute_linear_momentum = 5.43242364e-20)
    
    def test_linear_momentum_three_values() -> None:
        with pytest.raises(AssertionError):
            a = TimeStep(Linear_momentum = (1, 4, 5, 6), Time = 8.190e-05, Current_number_of_parcels = 6380,
                      Current_mass_in_system = 4.23525746e-22, Linear_kinetic_energy = 2.41789442e-16,
                      Absolute_linear_momentum = 5.43242364e-20)
        with pytest.raises(AssertionError):
            a = TimeStep(Linear_momentum = (1, 4), Time = 8.190e-05, Current_number_of_parcels = 6380,
                      Current_mass_in_system = 4.23525746e-22, Linear_kinetic_energy = 2.41789442e-16,
                      Absolute_linear_momentum = 5.43242364e-20)

    def test_linear_momentum_tuple_of_floats() -> None:
        with pytest.raises(AssertionError):
            a = TimeStep(Linear_momentum = ("a", 5.0, {}), Time = 8.190e-05, Current_number_of_parcels = 6380,
                      Current_mass_in_system = 4.23525746e-22, Linear_kinetic_energy = 2.41789442e-16,
                      Absolute_linear_momentum = 5.43242364e-20)

class TestAbsoluteLinearMomentum():
    Absolute_linear_momentum = 5.43242364e-20
    Linear_momentum = (-1.44664513e-21, -1.94003635e-21, -5.42703062e-20)

    def test_absolute_linear_momentum_exists(self) -> None:
        a = TimeStep(Absolute_linear_momentum = self.Absolute_linear_momentum, Time = 8.190e-05, Current_number_of_parcels = 6380,
                      Current_mass_in_system = 4.23525746e-22, Linear_kinetic_energy = 2.41789442e-16, 
                      Linear_momentum = (-1.44664513e-21, -1.94003635e-21, -5.42703062e-20))
    
    def test_absolute_linear_momentum_is_float() -> None:
        with pytest.raises(AssertionError):
            a = TimeStep(Absolute_linear_momentum = "a", Time = 8.190e-05, Current_number_of_parcels = 6380,
                      Current_mass_in_system = 4.23525746e-22, Linear_kinetic_energy = 2.41789442e-16, 
                      Linear_momentum = (-1.44664513e-21, -1.94003635e-21, -5.42703062e-20))
            
    def test_absolute_linear_momentum_gt_zero():
        with pytest.raises(AssertionError):
            a = TimeStep(Absolute_linear_momentum = -0.001, Time = 8.190e-05, Current_number_of_parcels = 6380,
                      Current_mass_in_system = 4.23525746e-22, Linear_kinetic_energy = 2.41789442e-16, 
                      Linear_momentum = (-1.44664513e-21, -1.94003635e-21, -5.42703062e-20))

    def test_absolute_linear_mumentum_eq_linear_momentum(self):
        a = TimeStep(Linear_momentum = self.Linear_momentum, Absolute_linear_momentum = self.Absolute_linear_momentum, Time = 8.190e-05, 
                     Current_number_of_parcels = 6380, Current_mass_in_system = 4.23525746e-22, Linear_kinetic_energy = 2.41789442e-16)
        for i in TimeStep.Linear_momentum:
            c = c + i**2
        c = c**0.5
        assert c == a.Absolute_linear_momentum
class TestLinearKineticEnergy():
    Linear_kinetic_energy = 2.41789442e-16

    def test_Linear_kinetic_energy_exists(self):
        a = TimeStep(Linear_kinetic_energy = self.Linear_kinetic_energy, Absolute_linear_momentum = 5.43242364e-20, Time = 8.190e-05, 
                     Current_number_of_parcels = 6380, Current_mass_in_system = 4.23525746e-22, 
                     Linear_momentum = (-1.44664513e-21, -1.94003635e-21, -5.42703062e-20))

    def test_Linear_kinetic_energy_gt_zero():
        a = TimeStep(Linear_kinetic_energy = -5.525, Absolute_linear_momentum = 5.43242364e-20, Time = 8.190e-05, 
                     Current_number_of_parcels = 6380, Current_mass_in_system = 4.23525746e-22, 
                     Linear_momentum = (-1.44664513e-21, -1.94003635e-21, -5.42703062e-20))
    
    def test_Linear_kinetic_energy_float():
        a = TimeStep(Linear_kinetic_energy = "a", Absolute_linear_momentum = 5.43242364e-20, Time = 8.190e-05, 
                     Current_number_of_parcels = 6380, Current_mass_in_system = 4.23525746e-22, 
                     Linear_momentum = (-1.44664513e-21, -1.94003635e-21, -5.42703062e-20))