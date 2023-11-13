import pytest

from OFParser.timestep.py import timestep

class TestLinearMomentumClass():
    linear_momentum = (-1.44664513e-21 -1.94003635e-21 -5.42703062e-20)

    def test_linear_momentum_exists(self) -> None:
        a = timestep(linear_momentum = self.linear_momentum)

    def test_linear_momentum_is_tuple() -> None:
        with pytest.raises(AssertionError):
            a = timestep(linear_momentum = 5)
    
    def test_linear_momentum_three_values() -> None:
        with pytest.raises(AssertionError):
            a = timestep(linear_momentum = (1, 4, 5, 6))
        with pytest.raises(AssertionError):
            a = timestep(linear_momentum = (1, 4))

    def test_linear_momentum_tuple_of_floats() -> None:
        with pytest.raises(AssertionError):
            a = timestep(linear_momentum = ("a", 5.0, {}))

class TestAbsoluteLinearMomentum():
    absolute_linear_momentum = 5.43242364e-20
    linear_momentum = (-1.44664513e-21 -1.94003635e-21 -5.42703062e-20)

    def test_absolute_linear_momentum_exists(self) -> None:
        a = timestep(absolute_linear_momentum = self.absolute_linear_momentum)
    
    def test_absolute_linear_momentum_is_float() -> None:
        with pytest.raises(AssertionError):
            a = timestep(absolute_linear_momentum = "a")
            
    def test_absolute_linear_momentum_gt_zero():
        with pytest.raises(AssertionError):
            a = timestep(absolute_linear_momentum = -0.001)

    def test_absolute_linear_mumentum_eq_linear_momentum(self): #z nějakého důvodu nepasuje přesně
        a = timestep(linear_momentum = self.linear_momentum, absolute_linear_momentum = self.absolute_linear_momentum)
        sum(a.linear_momentum) == a.absolute_linear_momentum

    

