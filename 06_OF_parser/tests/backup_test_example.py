import pytest

from OFParser.example import dcExample

# dataclass dcExample
#   - label: str
#   - count: int

class TestClass():
    label = 'a'
    count = 5

    def test_init(self):
        a = dcExample(label=self.label,count=self.count)

    def test_repr(self):
        a = dcExample(label=self.label,count=self.count)
        assert str(a) == "dcExample(label='a', count=5)"

def test_label_type() -> None:
    with pytest.raises(AssertionError):
        a = dcExample(label=1,count=5)

def test_count_type() -> None:
    with pytest.raises(AssertionError):
        a = dcExample(label='a',count=5.0)

def test_n_params() -> None:
    with pytest.raises(TypeError):
        a = dcExample('a',5,6)

def test_prepared() -> None:
    a = dcExample(label='a',count=5)
    b = a.prepare_data_for_plot([1,2,3])
    assert b == [2,3,4]