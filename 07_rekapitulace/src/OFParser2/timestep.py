from dataclasses import dataclass


@dataclass
class TimeStep:
    time: float
    current_number_of_parcels: int
    current_mass_in_system: float
    linear_momentum: tuple[float, float, float]
    linear_kinetic_energy: float

    @classmethod
    def from_str(cls, text: str):
        pass
    