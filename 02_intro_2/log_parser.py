"""
This module contains the functionality for parsing the log files from the 'particleInEB' simulation.
Each simulation step is identified by a line matching the `STEP_TIME_PATTERN` regex pattern. The step time 
itself captured by this regex group.
A number of other variables is parsed from each simulation step. Which variables are parsed is controlled solely 
by the `STEP_DATA_PATTERNS` dictionary. Each key in this dictionary corresponds to a variable, and the value is
the regex pattern for capturing the variable from the log file. The regex patterns contained in this dictionary
must each have a single group, which captures the value of the variable. More than a single variable might be parsed
from a single log line, but each variable must be captured by its own regex pattern.
"""

from pathlib import Path
import re

import pandas as pd


# regex pattern for identification of the start of the step and for capturing the simulation time:
STEP_TIME_PATTERN = re.compile(r"^Time = (.+)$")
# regex patterns for capturing the data from a single step - one key for each variable captured:
STEP_DATA_PATTERNS = {
    "num_parcels": re.compile(r"\s+Current number of parcels\s+= (\d+)"),
    "mass": re.compile(r"\s+Current mass in system\s+= (.+)$"),
    "avg_momentum": re.compile(r"\s+\|Linear momentum\|\s+= (.+)$"),
    "kin_energy": re.compile(r"\s+Linear kinetic energy\s+= (.+)$"),
    "parcels_added": re.compile(r"\s+number of parcels added\s+= (\d+)"),
    "mass_added": re.compile(r"\s+mass introduced\s+= (.+)$"),
    "parcels_escaped": re.compile(r"\s+- escape\s+= (\d+), .+"),
    "mass_escaped": re.compile(r"\s+- escape\s+= \d+, (.+)$"),
    "execution_time": re.compile(r"^ExecutionTime = (.+) s\s+ClockTime = \d+ s$"),
}
# optional data types for the parsed variables - if not specified, the default will be float:
DATA_TYPES = {
    "num_parcels": int,
    "parcels_added": int,
    "parcels_escaped": int,
}


def parse_log(log_path: Path | str) -> pd.DataFrame:
    """A function for parsing the log file from the 'particleInEB' simulation.

    Args:
        log_path: The path to the log file.

    Returns:
        A pandas time series dataframe containing the parsed data. The frame is indexed by the simulation step time
        and each column corresponds to a single variable, defined as a key in the `STEP_DATA_PATTERNS` dictionary.
    """
    # house keeping and initialization:
    log_path = Path(log_path)
    log_data = pd.DataFrame(columns=STEP_DATA_PATTERNS.keys())
    log_data.index.name = "time"

    # read the log file into a list of lines:
    with log_path.open() as f:
        log = f.readlines()

    # initialize the time variable to a negative value:
    time = -1
    # read the file line by line, and try to match all the regex patterns to each line
    for log_line in log:
        if STEP_TIME_PATTERN.match(log_line):
            # if the line matches the time pattern, update the time variable
            time = float(STEP_TIME_PATTERN.match(log_line).group(1))
            continue
        for key, pattern in STEP_DATA_PATTERNS.items():
            if pattern.match(log_line):
                # if the line matches the pattern, update the corresponding column in the log_data dataframe
                dtype = DATA_TYPES.get(key, float)
                log_data.loc[time, key] = dtype(pattern.match(log_line).group(1))

    return log_data


if __name__ == "__main__":
    import sys

    print(parse_log(sys.argv[1]))
