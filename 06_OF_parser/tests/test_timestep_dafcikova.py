from OFParser.timestep import TimeStep
import pytest

# Current number of parcels
# existuje?
# zparsujeme "log_example", je "Current number of parcels" rovny 6380 ?
# jde o int?
# je nezaporny?

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
    
