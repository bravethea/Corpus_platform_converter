import argparse
import json
import os

import conllu_parse
# from . import conllu_parse # TV: I am not sure how this is supposed to work, I am getting an ImportError

class Converter:

    def __init__(self, unknown_data_path, output_file = None):
        if os.path.isfile(unknown_data_path):
            self.unknown_data_path = unknown_data_path
        else:
            raise ImportError("The specified file does not exist.")

        if output_file == None:
            self.output_file = open("output_files/json_out.json", 'w')
        else:
            self.output_file = open(output_file, 'w')


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
            return conllu_parsed


    def save_output(self):
        parsed_dict = self.parse_input()
        saved_output = json.dump(parsed_dict, self.output_file)
        print("saved")
        return saved_output




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert input file (arg1) into output file (arg2)")
    parser.add_argument("-in", "--input_file", type=str, required=True, help="Input file path")
    parser.add_argument("-out", "--output_file", type=str, help="Output file path")
    args = parser.parse_args()

    converter = Converter(args.input_file, args.output_file)
    Converter.save_output(converter)
