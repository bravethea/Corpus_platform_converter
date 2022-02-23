import argparse
import json
import os

import conllu_parse
# from . import conllu_parse # TV: I am not sure how this is supposed to work, I am getting an ImportError

class Converter:

    def __init__(self, unknown_data_path, output_file = None):
        self.unknown_data_path = unknown_data_path
        self.output_file = output_file

    def determine_format(self):
        if os.path.isfile(self.unknown_data_path):
            if self.unknown_data_path.endswith(".conllu"):
                input_format = "conllu"
                return input_format
            elif self.unknown_data_path.endswith(".vert"):
                input_format = "vert"
                return input_format
            elif self.unknown_data_path.endswith(".xml"):
                input_format = "xml"
                return input_format
            else:
                raise ValueError("Unrecognized format. \n Note: The converter currently supports the following formats: .conllu, .xml (TEI), and .vert.")

    def parse_input(self):
        input_format = self.determine_format()
        if input_format == "conllu":
            conllu_parsed = conllu_parse.parser(self.unknown_data_path)

    def save_output(self):
        parsed_dict = self.parse_input(self.unknown_data_path)
        with open(self.output_file, 'w') as out_file:
            json.dump(out_file, parsed_dict)




if __name__ == "__main__":

    conllu_path = "/Users/teodoravukovic/Google Drive (not syncing)/PycharmProjects/VIAN-file-conversion/CONLLU/samples/conllu_test.conllu"  # this line should be within the main block

    Converter(conllu_path, output_file="json_text.json")
