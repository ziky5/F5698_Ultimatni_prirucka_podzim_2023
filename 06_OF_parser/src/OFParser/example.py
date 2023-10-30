from dataclasses import dataclass

@dataclass
class dcExample():
    label: str
    count: int

    def __post_init__(self):
        assert isinstance(self.label, str)
        assert isinstance(self.count, int)

    def prepare_data_for_plot(self, lst):
        return lst + 1