import io

from pydot import graph_from_dot_data
from textx.export import model_export_to_file

from plparser.modules.parser import WFF


def write_png_from_wff(wff: WFF, filename: str) -> None:
    dot_file = io.StringIO()
    model_export_to_file(dot_file, wff)
    (graph,) = graph_from_dot_data(dot_file.getvalue())
    graph.write_png(f"{filename}.png")
