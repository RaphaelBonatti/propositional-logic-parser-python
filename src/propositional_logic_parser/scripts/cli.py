import argparse

from modules.parser import wff_from_str
from modules.visualizer import write_png_from_wff


def parse_args():
    parser = argparse.ArgumentParser(
        prog="wff_visualizer",
        description="Enter a wff as string and visualize the parsed tree as png.",
    )
    parser.add_argument("wff", type=str)
    parser.add_argument(
        "-p", "--print", action="store_true", help="print a formatted wff"
    )
    parser.add_argument(
        "-g",
        "--generate",
        metavar="FILENAME",
        help="give a name and generate a png representing an ast of the wff",
        type=str,
    )
    return parser.parse_args()


def entrypoint():
    args = parse_args()
    wff_str = args.wff
    wff = wff_from_str(wff_str)
    if args.print:
        print(f"Well-formed formula: {wff.toString()}")
    if args.generate:
        filename = args.generate
        write_png_from_wff(wff, args.generate)
        print(f"The image {filename}.png has been generated.")


if __name__ == "__main__":
    entrypoint()
