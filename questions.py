from pylatex.base_classes.containers import Environment
from pylatex.package import Package

class Questions(Environment):
    """
    A class for the Questions environment
    """
    packages = [Package('alltt')]
    escpae = False
    content_separator = '\n'

    # def __init__(self):
    #     BEGIN_CODE = "\begin{center}"
    #     END_CODE = "\begin{center}"
    #     super(Questions, self).__init__()


