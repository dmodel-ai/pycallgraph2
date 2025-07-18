
from .output import Output
import json

class JsonOutput(Output):
    def __init__(self, **kwargs):
        self.output_file = 'pycallgraph.json'
        Output.__init__(self, **kwargs)
    @classmethod
    def add_arguments(cls, subparsers, parent_parser, usage):
        defaults = cls()
        subparser = subparsers.add_parser(
            'json', help='Graphviz generation',
            parents=[parent_parser], usage=usage,
        )
        cls.add_output_file(
            subparser, defaults, 'The generated JSON file'
        )
        pass
    def done(self) -> None:
        with open(self.output_file, 'w') as f:
            for src_func, dests in self.processor.call_dict.items():
                if not src_func:
                    continue
                print(json.dumps({src_func: list(dests.keys())}),
                      file=f)

        pass
