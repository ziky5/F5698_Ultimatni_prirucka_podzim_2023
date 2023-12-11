from dataclasses import dataclass
from typing import Sequence
import re

from OFParser2.timestep import TimeStep


def parse(data: str) -> Sequence[TimeStep]:
    split = re.split(r"(Time = \d\.\d+e-\d+\n)", data)
    # get rid of empty strings
    split = [chunk for chunk in split if chunk]

    tss = []

    # iterujeme po dvojicich, nebot sudy element je radek s "Time = " a lichy
    # jsou data pro TimeStep
    for i in range(1, len(split), 2):
        tss.append(TimeStep.from_str(split[i] + split[i + 1]))

    return tss
