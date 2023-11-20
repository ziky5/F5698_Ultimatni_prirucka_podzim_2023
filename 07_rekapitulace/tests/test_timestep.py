from OFParser2.timestep import TimeStep


ts_kwargs = dict(
    time=1.0,
    current_number_of_parcels=10,
    current_mass_in_system=4.5,
    linear_momentum=(2.0, 2.0, 1.0),
    linear_kinetic_energy=1.0,
)


def test_timestep():
    ts = TimeStep(**ts_kwargs)
