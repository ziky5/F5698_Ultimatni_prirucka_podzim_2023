import pytest
from OFParser2.timestep import TimeStep

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
]


@pytest.fixture(params=bad_timestep_data)
def timestep_bad_data(request):
    return request.param


def test_bad_timestep(timestep_bad_data):
    ts_kwargs, exc_type, exc_msg = timestep_bad_data
    with pytest.raises(exc_type) as e:
        TimeStep(**ts_kwargs)

    assert e.value.args[0] == exc_msg
