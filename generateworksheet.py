from argparse import ArgumentParser
from pylatex import Document, Section, Subsection, Math
from pylatex.utils import bold

GEOMETRY_OPTIONS = dict(tmargin="1cm", lmargin="10cm")

def generate_worksheet(output_path):
    """
    Build the PDF document
    """

    doc = Document(f'{output_path}/doc', geometry_options=GEOMETRY_OPTIONS)

    with doc.create(Section('The simple stuff')):
        doc.append('Some regular text and some')
        doc.append(bold('italic text. '))
        doc.append('\nAlso some crazy characters: $&#{}')

        with doc.create(Subsection('Math that is incorrect')):
            doc.append(Math(data=['2*3', '=', 9]))
    
    doc.generate_pdf(f'{output_path}/full', clean_tex=False)


if __name__ == "__main__":
    description = """A python program to compile LaTex documents"""
    parser = ArgumentParser(description=description)
    parser.add_argument('OUTPUT_DIR', help="The dircotry in which to store the compiled PDF")
    args = parser.parse_args()

    generate_worksheet(args.OUTPUT_DIR)