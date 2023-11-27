from dataclasses import dataclass


class CompError(Exception):
    pass


@dataclass
class TimeStep:
    time: float
    current_number_of_parcels: int
    current_mass_in_system: float
    linear_momentum: tuple[float, float, float]
    linear_kinetic_energy: float

    def __post_init__(self):
        self.time = float(self.time)
        assert self.time >= 0.0, "value of 'time' can not be < 0"
        current_number_of_parcels = int(float(self.current_number_of_parcels))
        # TODO: comment
        assert current_number_of_parcels == float(
            self.current_number_of_parcels
        ), "value of 'current_number_of_parcels' must be an integer"
        self.current_number_of_parcels = current_number_of_parcels
        assert (
            self.current_number_of_parcels >= 0
        ), "value of 'current_number_of_parcels' can not be < 0"
        self.current_mass_in_system = float(self.current_mass_in_system)
        assert (
            self.current_mass_in_system >= 0.0
        ), "value of 'current_mass_in_system' can not be < 0"
        assert hasattr(
            self.linear_momentum, "__iter__"
        ), "object type of 'linear_momentum' must be iterable"
        self.linear_momentum = tuple([float(v) for v in self.linear_momentum])
        assert (
            len(self.linear_momentum) == 3
        ), "object 'linear_momentum' must consist of exactly three parameters"
        self.linear_kinetic_energy = float(self.linear_kinetic_energy)
        assert (
            self.linear_kinetic_energy >= 0.0
        ), "value of 'linear_kinetic_energy' can not be < 0"

    @classmethod
    def from_str(cls, text: str):
        pass
