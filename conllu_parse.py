import codecs
import re

"""
ID: Word index, integer starting at 1 for each new sentence; may be a range for multiword tokens; may be a decimal number for empty nodes (decimal numbers can be lower than 1 but must be greater than 0).
FORM: Word form or punctuation symbol.
LEMMA: Lemma or stem of word form.
UPOS: Universal part-of-speech tag.
XPOS: Language-specific part-of-speech tag; underscore if not available.
FEATS: List of morphological features from the universal feature inventory or from a defined language-specific extension; underscore if not available.
HEAD: Head of the current word, which is either a value of ID or zero (0).
DEPREL: Universal dependency relation to the HEAD (root iff HEAD = 0) or a defined language-specific subtype of one.
DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs.
MISC: Any other annotation.
"""


def parser(conllu_path):

    with codecs.open(conllu_path, 'r', 'utf8') as input_file:

        conllu_parsed = {
            "metadata_file" : {},
            "sentences" : {}
        }

        input_data = input_file.read()
        sentences = [sent for sent in input_data.split('\n\n') if sent]

        for sent in sentences:
            sent_list = [line for line in sent.split('\n') if line]
            for line in sent_list:
                if line.startswith('#'):
                    if 'sent_id' in line:
                        sent_id = line.split('=')[-1].strip()

                conllu_parsed["sentences"][sent_id] = {}

            for line in sent_list:
                if not line.startswith('#'):
                    line_list = line.split('\t')
                    conllu_parsed["sentences"][sent_id]["token_id"] = line_list[0]
                    conllu_parsed["sentences"][sent_id]["word"] = line_list[1]
                    conllu_parsed["sentences"][sent_id]["lemma"] = line_list[2]
                    conllu_parsed["sentences"][sent_id]["upos"] = line_list[3]
                    conllu_parsed["sentences"][sent_id]["xpos"] = line_list[4]
                    conllu_parsed["sentences"][sent_id]["feats"] = line_list[4]
                    conllu_parsed["sentences"][sent_id]["head"] = line_list[5]
                    conllu_parsed["sentences"][sent_id]["deprel"] = line_list[6]
                    conllu_parsed["sentences"][sent_id]["deps"] = line_list[7]

        return conllu_parsed


conllu_path = "/Users/teodoravukovic/Google Drive (not syncing)/PycharmProjects/VIAN-file-conversion/CONLLU/samples/conllu_test.conllu"
parser(conllu_path)