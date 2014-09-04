#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from argparse import ArgumentParser
from jinja2 import Environment, FileSystemLoader
import yaml
import os.path


class Loader(yaml.Loader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with codecs.open(filename, 'r', 'utf-8') as f:
            return yaml.load(f, Loader)

Loader.add_constructor('!include', Loader.include)


if __name__ == "__main__":
	parser = ArgumentParser(description='Render Jinja2 template from JSON data')

	parser.add_argument('-i', action="store", dest="infile", help="JSON input data")
	parser.add_argument('-t', action="store", dest="template", help="Jinja2 template")
	parser.add_argument('-o', action="store", dest="outfile", help="output file")

	parsed_results = parser.parse_args()

	env = Environment(loader=FileSystemLoader("."))
	template = env.get_template( parsed_results.template )

	infile = codecs.open(parsed_results.infile, 'r', 'utf-8')
	outfile = codecs.open(parsed_results.outfile, 'w', 'utf-8')
	outfile.write( template.render( yaml.load(infile, Loader) ) )
