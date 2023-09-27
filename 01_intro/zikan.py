# %%
import re

import numpy
import pandas as pd
import plotly.graph_objects as go


def parse_log(path_to_log):
    with open(path_to_log) as f:
        text = f.read()

    split = re.split("(Time = \d\.\d+e-\d+\n)", text)

    data = {}

    for rec in split[1:]:
        if len(rec.strip().split("\n")) == 1 and "Time = " in rec:
            time = float(rec.strip().split("=")[1])
            data[time] = {}
            continue

        for line in rec.split("\n"):
            number_of_equal_signs = line.count("=")
            if number_of_equal_signs == 1:
                l, r = line.split("=")
                l = l.strip()
                r = r.strip()
                data[time][l] = r

    return data


# %%
data = parse_log("log.ParticleInEB")
df = pd.DataFrame(data).T
fig = go.Figure()
fig.add_trace(
    go.Scatter(x=df.index, y=df["Current number of parcels"].astype(float).values)
)
fig.show()

# %%
