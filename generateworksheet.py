from argparse import ArgumentParser
from pylatex.utils import bold

from worksheet import Worksheet

def generate_worksheet(output_path):
    """
    Build the PDF document
    """

    doc = Worksheet(output_path)

    doc.fill_document()
    doc.add_question()
    doc.generate_pdf(output_path, clean_tex=False)


if __name__ == "__main__":
    description = """A python program to compile LaTex documents"""
    parser = ArgumentParser(description=description)
    parser.add_argument('OUTPUT_PATH', help="The dircotry in which to store the compiled PDF")
    args = parser.parse_args()

    generate_worksheet(args.OUTPUT_PATH)