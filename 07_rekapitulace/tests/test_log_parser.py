from OFParser2.log_parser import parse
from OFParser2.timestep import TimeStep

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

Time = 8.195e-05

Evolving kinematicCloud

Solving 3-D cloud kinematicCloud
Cloud: kinematicCloud
    Current number of parcels       = 6381
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

Time = 8.200e-05

Evolving kinematicCloud

Solving 3-D cloud kinematicCloud
Cloud: kinematicCloud
    Current number of parcels       = 6382
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


def test_log_parser():
    tss = parse(DATA)

    assert tss[0] == TimeStep(
        time=8.190e-05,
        current_number_of_parcels=6380,
        current_mass_in_system=4.23525746e-22,
        linear_momentum=(-1.44664513e-21, -1.94003635e-21, -5.42703062e-20),
        linear_kinetic_energy=2.41789442e-16,
    )
    assert tss[1] == TimeStep(
        time=8.195e-05,
        current_number_of_parcels=6381,
        current_mass_in_system=4.23525746e-22,
        linear_momentum=(-1.44664513e-21, -1.94003635e-21, -5.42703062e-20),
        linear_kinetic_energy=2.41789442e-16,
    )
    assert tss[2] == TimeStep(
        time=8.200e-05,
        current_number_of_parcels=6382,
        current_mass_in_system=4.23525746e-22,
        linear_momentum=(-1.44664513e-21, -1.94003635e-21, -5.42703062e-20),
        linear_kinetic_energy=2.41789442e-16,
    )
