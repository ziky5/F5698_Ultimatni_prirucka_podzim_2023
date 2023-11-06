# %%
# Import
import pytest
from OFParser.kolar import Data as dt
from OFParser.kolar import a
import numpy as np
# %%

# class Data():
#    time: float    # Time
#    count: int     # Particle counter ("Current number of parcels")
#    mass: float    # Mass ("Current mass in system")
#    mmt: float     # Linear momentum
#    absmmt: float  # Abs of linear momentum
#    en: float      # Energy ("Linear kinetic energy")
#    extime: float  # Execution time

# Je to stále docela ošemetné a příliš konkrétní...
# Nejprve zkouším testovat vytvořenou dataclassu "a", která by měla splňovat všechny parametry:

def test_time_s_type():
    a = dt(time = 20.15, count = 50000, mass = 2.0, mmt = 865.0, absmmt = 865.0, en = 300.0, extime = 0.0001)
    assert type(a.time) == float

def test_count_s_type() -> None:
    assert type(a.count) == int

def test_mass_s_type() -> None:
    assert type(a.mass) == float

def test_mmt_s_type() -> None:
    assert type(a.mmt) == float

def test_absmmt_s_type() -> None:
    assert type(a.absmmt) == float

def test_en_s_type() -> None:
    assert type(a.en) == float

def test_extime_s_type() -> None:
    assert type(a.extime) == float

def test_time_existence() -> None:
    a.time


    a.count
    a.mass
    a.mmt
    a.absmmt
    a.en
    a.extime

# Potom se snažím o nějakou obecnou definici dataclassy
# Následující se nesplní, protože potřebují více argumentů -- jakým způsobem že se to dělá, aby ta dataclassa nepotřebovala argumenty? :-)

def test_class_type() -> None:
        with pytest.raises(TypeError):
            d = dt(time = 20)

def test_time_type() -> None:
        with pytest.raises(AssertionError):
            d = dt(time = 20, count = 50000, mass = 2.0, mmt = 865.0, absmmt = 865.0, en = 300.0, extime = 0.0001)

def test_time_noneg() -> None:
        with pytest.raises(AssertionError):
            d = dt(time = -1.5)

def test_count_type() -> None:
        with pytest.raises(AssertionError):
            d = dt(count = 1.5)
# atd...

def test_aproximate_type() -> None:
    value = 4.23525746e-22
    assert np.all()

def test_read_and_init() -> None:
     a = dt.read(path)
    

def test_read_and_init() -> None:
     a = dt.read(path)
     expected = ''
     assert str(a) == expected
     
# %%
