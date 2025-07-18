import collections

from .output import Output
from .graphviz import GraphvizOutput
from .json import JsonOutput
from .gephi import GephiOutput
from .ubigraph import UbigraphOutput
from .pickle import PickleOutput


outputters = collections.OrderedDict([
    ('graphviz', GraphvizOutput),
    ('gephi', GephiOutput),
    ('json', JsonOutput),
    # ('ubigraph', UbigraphOutput),
])
