from pylatex import Document, Command, Section, Subsection
from pylatex.utils import italic, NoEscape

from questions import Questions
from parts import Parts

class Worksheet(Document):
    """
    Class to handle the Worksheet
    """
    EXAM_CLASS = 'exam'
    EXAM_OPTIONS = ['a4paper', 'answers']

    def __init__(self, output_path):    
        super(Worksheet, self).__init__(output_path,
                                        documentclass=self.EXAM_CLASS,
                                        document_options=self.EXAM_OPTIONS)
        self._build_preamble()

    def _build_preamble(self):
        """
        The required preamble to set up document
        """
        self.preamble.append(Command('title', 'Worksheet'))
        self.preamble.append(Command('author', 'Gaps And Posts'))
        self.preamble.append(Command('date', NoEscape(r'\today')))
        self.append(NoEscape(r'\maketitle'))

    def add_question(self):
        with self.create(Questions()):
            self.append(Command('question', 'Hello this is a quesiton'))
            self.add_part()

    
    def add_part(self):
        with self.create(Parts()):
            self.append(Command('part', 'Is this is a part?'))

    def fill_document(self):
        """Add a section, a subsection and some text to the document."""
        with self.create(Section('A section')):
            self.append('Some regular text and some ')
            self.append(italic('italic text. '))

            with self.create(Subsection('A subsection')):
                self.append('Also some crazy characters: $&#{}')
