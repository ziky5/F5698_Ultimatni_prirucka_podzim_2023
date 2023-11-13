import pytest

from OFParser.TimeStep import TimeStep

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
    

