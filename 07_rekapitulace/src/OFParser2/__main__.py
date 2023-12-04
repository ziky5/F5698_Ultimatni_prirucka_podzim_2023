import click
import OFParser2.log_parser
import plotly.graph_objects as go


# @click.command()
# @click.argument("filename", type=click.Path(exists=True))
# @click.option("--attr", default="current_number_of_parcels", help="Attribute to parse.")
# def parse(filename, attr):
#     """Parse log file and print attribute. FILENAME is path to log file."""
#     with open(filename) as f:
#         tss = OFParser2.log_parser.parse(f.read())
#     print([(ts.time, getattr(ts, attr)) for ts in tss])


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option("--attr", default="current_number_of_parcels", help="Attribute to parse.")
@click.option(
    "--ticks-font-size", default=18, help="Font size for the ticks on the axes."
)
def parse(filename, attr, ticks_font_size):
    """Parse log file and plot attribute. FILENAME is path to log file."""
    with open(filename) as f:
        tss = OFParser2.log_parser.parse(f.read())

    # Extract time and attribute values
    times = [ts.time for ts in tss]
    attrs = [getattr(ts, attr) for ts in tss]

    # Create a scatter plot
    fig = go.Figure(data=go.Scatter(x=times, y=attrs))

    # Update xaxis to use scientific notation and set tick font size
    fig.update_xaxes(tickformat=".2e", tickfont=dict(size=ticks_font_size))

    # Update yaxis to set tick font size
    fig.update_yaxes(tickfont=dict(size=ticks_font_size))

    # Show the plot
    fig.show()


def main():
    parse()
