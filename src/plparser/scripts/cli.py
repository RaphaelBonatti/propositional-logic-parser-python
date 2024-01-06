import argparse

from plparser.modules.parser import wff_from_str
from plparser.modules.visualizer import write_png_from_wff


def parse_args():
    parser = argparse.ArgumentParser(
        prog="wff_visualizer",
        description="Enter a wff as string and visualize the parsed tree as png.",
    )
    parser.add_argument("wff")
    parser.add_argument(
        "-p", "--print", action="store_true", help="print a formatted wff"
    )
    parser.add_argument(
        "-g",
        "--generate",
        action="store_true",
        help="generate a png representing an ast of the wff",
    )
    return parser.parse_args()


def entrypoint():
    args = parse_args()
    wff_str = args.wff
    wff = wff_from_str(wff_str)
    if args.print:
        print(f"Well-formed formula: {wff.toString()}")
    if args.generate:
        write_png_from_wff(wff)
        print("The image wff.png has been generated in the project's root directory.")


if __name__ == "__main__":
    entrypoint()
