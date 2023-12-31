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
        "could not convert string to float: 'NO'",
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
    # (
    #     dict(
    #         time=1.0,
    #         current_number_of_parcels=10,
    #         current_mass_in_system=2000.0,
    #         linear_momentum=(2.0, 2.0, 1.0),
    #         linear_kinetic_energy=1.0,
    #     ),
    #     CompError,
    #     "the physical interconnection of 'current_mass_in_system' and 'current_number_of_parcels' must be taken into account",
    # ),
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
        "object type of 'linear_momentum' must be iterable",
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
        TypeError,
        "float() argument must be a string or a real number, not 'tuple'",
    ),
    #     (
    #         dict(
    #             time=1.0,
    #             current_number_of_parcels=10,
    #             current_mass_in_system=4.5,
    #             linear_momentum=(2.0, 2.0, 1.0),
    #             linear_kinetic_energy=1000.0,
    #         ),
    #         CompError,
    #         "the physical interconnection of 'linear_momentum' and 'linear_kinetic_energy' must be taken into account",
    #     ),
]


@pytest.fixture(params=bad_timestep_data)
def timestep_bad_data(request):
    return request.param


def test_bad_timestep(timestep_bad_data):
    ts_kwargs, exc_type, exc_msg = timestep_bad_data
    with pytest.raises(exc_type) as e:
        TimeStep(**ts_kwargs)

    assert e.value.args[0] == exc_msg


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


def test_from_str():
    ts = TimeStep.from_str(DATA)
    assert ts == TimeStep(
        time=8.190e-05,
        current_number_of_parcels=6380,
        current_mass_in_system=4.23525746e-22,
        linear_momentum=(-1.44664513e-21, -1.94003635e-21, -5.42703062e-20),
        linear_kinetic_energy=2.41789442e-16,
    )
