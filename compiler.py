from argparse import ArgumentParser

TEX_FILE = 'basic.tex'

def compile(output_dir):
    """
    Function to compile the LaTex file into a PDF
    """
    return

if __name__ == "__main__":
    description = """A python program to compile LaTex documents"""
    parser = ArgumentParser(description=description)
    parser.add_argument('OUTPUT_DIR', help="The dircotry in which to store the compiled PDF")
    args = parser.parse_args()
    OUTPUT_DIR = args.OUTPUT_DIR

    compile(OUTPUT_DIR)