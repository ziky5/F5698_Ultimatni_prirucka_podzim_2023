from dataclasses import dataclass, field

@dataclass
class log_parse():
    Time: float = field(default=None)
    Current_number_of_parcels: int = field(default=None)
    Current_mass_in_system: float = field(default=None)
    Linear_momentum: tuple = field(default_factory=tuple)
    Absolute_linear_momentum: float = field(default=None)
    Linear_kinetic_energy: float = field(default=None)
    number_of_parcels_added: int = field(default=None)
    mass_introduced: float = field(default=None)
    escape: tuple = field(default_factory=tuple)
    stick: tuple = field(default_factory=tuple)
    ExecutionTime: float = field(default=None)
    ClockTime: int = field(default=None)





k_log = log_parse(
    Time = 2.000e-07,
    Current_number_of_parcels = 499847,
    Current_mass_in_system = 3.31815163e-20,
    Linear_momentum = (5.21616996e-22, 2.48209936e-21, -9.31938771e-18),
    Absolute_linear_momentum = 9.31938806e-18,
    Linear_kinetic_energy = 1.73101634e-15,
    number_of_parcels_added = 500000,
    mass_introduced = 3.31916729e-20,
    escape = (153, 1.01566519e-23),
    stick = (0, 0),
    ExecutionTime = 642.2,
    ClockTime = 643)
#print(k_log)