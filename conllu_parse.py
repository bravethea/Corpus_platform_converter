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
                    sent_id = sent_list[0].split('=')[1].strip(' ')

            conllu_parsed["sentences"][sent_id] = {"sent_metadata":{}, "sent_text":[]}

            for line in sent_list:
                if line.startswith('#'):
                    key = sent_list[0].split('=')[0].strip('#').strip(' ')
                    value = sent_list[0].split('=')[1].strip(' ')
                    conllu_parsed["sentences"][sent_id]["sent_metadata"][key] = value

                elif re.match(r'\d.*', line): # (token id can also be 1.a and other stuff)
                    line_list = line.split('\t')

                    id = line_list[0]
                    form = line_list[1]
                    lemma = line_list[2]
                    upos = line_list[3]
                    xpos = line_list[4]
                    feats = line_list[5]
                    head = line_list[6]
                    deprel = line_list[7]
                    deps = line_list[8]
                    misc = line_list[9]

                    line_dict = {"id": id, "form": form, "lemma": lemma, "upos": upos, "xpos": xpos, "feats": feats, "head": head, "deprel": deprel, "deps": deps, "misc": misc}

                    conllu_parsed["sentences"][sent_id]["sent_text"].append(line_dict)



        # print(conllu_parsed)
        return conllu_parsed


def writer(input_dict, input_filename=None):

    conllu_file_list = []

    for sent_id,sent_data in input_dict["sentences"].items():

        for item in sent_data:
            if "metadata" in item:
                sent_meta = sent_data[item]
            elif "text" in item:
                sent_text = sent_data[item]

        for k,v in sent_meta.items():
            conllu_file_list.append("# {} = {}\n".format(k,v))

        for item in sent_text:
            pass




parser(conllu_path)

