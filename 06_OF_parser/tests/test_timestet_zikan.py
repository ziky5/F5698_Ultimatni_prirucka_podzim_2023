from OFParser.timestep import TimeStep

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
    assert ts.Time == 8.190e-5
    assert ts.Current_number_of_parcels == 6380
    assert ts.Current_mass_in_system == 4.23525746e-22
    assert ts.Linear_momentum == (-1.44664513e-21, -1.94003635e-21, -5.42703062e-20)
    assert ts.Absolute_linear_momentum == 5.43242364e-20
    assert ts.Linear_kinetic_energy == 2.41789442e-16
    assert ts.models["model1"].number_of_parcels_added == 500000
    assert ts.models["model1"].mass_introduced == 3.31916729e-20
    assert ts.ParcelFate["escape"] == (493620, 3.27681468e-20)
    assert ts.ParcelFate["stick"] == (0, 0)
