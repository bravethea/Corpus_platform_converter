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

conllu_path = "/Users/teodoravukovic/Google Drive (not syncing)/PycharmProjects/VIAN-file-conversion/CONLLU/samples/conllu_test.conllu"

def parser(conllu_path):

    with codecs.open(conllu_path, 'r', 'utf8') as input_file:

        input_data = input_file.read()
        sentences = [sent for sent in input_data.split('\n\n') if sent]

        conllu_parsed = {
            "metadata_file" : {},
            "sentences" : {}
        }

        for sent in sentences:

            sent_list = [line for line in sent.split('\n') if line]
            for line in sent_list:
                if "sent_id" in line:
                    sent_id = sent_list[0].split(' = ')[1] #sent id will not always be the first attribute, there might not spaces around = ; identify the lines introduced with #
                #check how metadata is encoded, check if there is a separate metadata file
                #the last column of the token line is additional optional metadata, which can have key-value pairs


            conllu_parsed["sentences"][sent_id] = []

            for line in sent_list:
                if re.match(r'\d.*', line): # if a line begins with # then it is a comment, every other line must be a row (token id can also be 1.a and other stuff)
                    line_list = line.split('\t')
                    conllu_parsed["sentences"][sent_id].append(line_list)

                        # token_id = line_list[0]
                        # word = line_list[1]
                        # lemma = line_list[2]
                        # upos = line_list[3]
                        # xpos = line_list[4]
                        # feats = line_list[4]
                        # head = line_list[5]
                        # deprel = line_list[6]
                        # deps = line_list[7]

        print(conllu_parsed)
        return conllu_parsed

parser(conllu_path)

