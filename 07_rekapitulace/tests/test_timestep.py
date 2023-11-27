import pytest
from OFParser2.timestep import TimeStep, CompError

timestep_ok = TimeStep(
    time=1.0,
    current_number_of_parcels=10,
    current_mass_in_system=4.5,
    linear_momentum=(2.0, 2.0, 1.0),
    linear_kinetic_energy=1.0,
)

ok_timestep_data = [
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        timestep_ok,
    ),
    (
        dict(
            time="1",
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        timestep_ok,
    ),
    (
        dict(
            time=1,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        timestep_ok,
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10.0,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        timestep_ok,
    ),
    (
        dict(
            time=1,
            current_number_of_parcels="10",
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        timestep_ok,
    ),
    (
        dict(
            time=1,
            current_number_of_parcels="10.0",
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        timestep_ok,
    ),
    (
        dict(
            time=1,
            current_number_of_parcels=10,
            current_mass_in_system="4.5",
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        timestep_ok,
    ),
    (
        dict(
            time=1,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2, 2, 1),
            linear_kinetic_energy=1.0,
        ),
        timestep_ok,
    ),
    (
        dict(
            time=1,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=("2.0", "2.0", "1.0"),
            linear_kinetic_energy=1.0,
        ),
        timestep_ok,
    ),
    (
        dict(
            time=1,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=[2.0, 2.0, 1.0],
            # toto je trochu odvážné, ale já mám listy rád :-)
            linear_kinetic_energy=1.0,
        ),
        timestep_ok,
    ),
    (
        dict(
            time=1,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1,
        ),
        timestep_ok,
    ),
    (
        dict(
            time=1,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy="1.0",
        ),
        timestep_ok,
    ),
]


@pytest.fixture(params=ok_timestep_data)
def timestep_data(request):
    return request.param


def test_timestep(timestep_data):
    ts_kwargs, test_ts = timestep_data
    ts = TimeStep(**ts_kwargs)
    assert ts == test_ts


bad_timestep_data = [
    (
        dict(
            time="NO",
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        ValueError,
        "could not convert string to float: 'NO'",
    ),
    (
        dict(
            time=-1.0,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        AssertionError,
        "value of 'time' can not be < 0",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10.5,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        AssertionError,
        "value of 'current_number_of_parcels' must be an integer",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=-10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        AssertionError,
        "value of 'current_number_of_parcels' can not be < 0",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels="NO",
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        ValueError,
        "could not convert string to int: 'NO'",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=-4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        AssertionError,
        "value of 'current_mass_in_system' can not be < 0",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=2000.0,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        CompError,
        "the physical interconnection of 'current_mass_in_system' and 'current_number_of_parcels' must be taken into account",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        AssertionError,
        "object 'linear_momentum' must consist of exactly three parameters",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        AssertionError,
        "object 'linear_momentum' must consist of exactly three parameters",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0, 1.0, 1.0),
            linear_kinetic_energy=1.0,
        ),
        AssertionError,
        "object 'linear_momentum' must consist of exactly three parameters",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=2.0,
            linear_kinetic_energy=1.0,
        ),
        AssertionError,
        "object type of 'linear_momentum' must be a tuple or a list",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=("NO", "NO", "NO"),
            linear_kinetic_energy=1.0,
        ),
        ValueError,
        "could not convert string to float: 'NO'",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=-1.0,
        ),
        AssertionError,
        "value of 'linear_kinetic_energy' can not be < 0",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=(2.0, 2.0, 1.0),
        ),
        AssertionError,
        "object type of 'linear_kinetic_energy' must be a float or int",
    ),
    (
        dict(
            time=1.0,
            current_number_of_parcels=10,
            current_mass_in_system=4.5,
            linear_momentum=(2.0, 2.0, 1.0),
            linear_kinetic_energy=1000.0,
        ),
        CompError,
        "the physical interconnection of 'linear_momentum' and 'linear_kinetic_energy' must be taken into account",
    ),
]


@pytest.fixture(params=bad_timestep_data)
def timestep_bad_data(request):
    return request.param


def test_bad_timestep(timestep_bad_data):
    ts_kwargs, exc_type, exc_msg = timestep_bad_data
    with pytest.raises(exc_type) as e:
        TimeStep(**ts_kwargs)

    assert e.value.args[0] == exc_msg
