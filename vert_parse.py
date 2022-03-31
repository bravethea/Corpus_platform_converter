import codecs
import re
import json
from lxml import etree

"""
<text id="TOR_C_0001">
<speech id="TOR_C_0001-u1" who="RS_DK" name="Dejan Krstić" gender="M" role_id="TOR_RS" role_name="Researcher">
pitáo	pitao	pitati-v	Vmp-sm
ljúbu	ljubu	ljuba-n	Ncfsa
on	on	on-p	Pp3msn
káže	kaže	kazati-v	Vmr3s
príčajte	pričajte	pričati-v	Vmm2p
[pause]			
kólko	kolko	koliki-p	Pq-nsn
óćete	oćete	hteti-v	Vmr2p
</speech>
<speech id="TOR_C_0001-u2" who="TIM_SPK_0001" name="-" gender="F" role_id="TOR_INF_D" role_name="Informant from the region, representative of the dialect">
he	he	he-n	Ncfpn
[pause]			
paa	paa	pa-c	Cc
ajdéte	ajdete	hajde-i	I
ovámo	ovamo	ovamo-r	Rgp
ví	vi	vi-p	Pp2-pn
</speech>
</text>

"""

def parser(vert_path):

    with codecs.open(vert_path, 'r', 'utf8') as input_file:
        input_data = input_file.read()

        root = etree.fromstring(input_data)
        # sentences = [sent for sent in input_data.split('>\n<s') if sent]

        vert_parsed = {
            "metadata_file": {},
            "sentences": {}
        }

        for element in root:

            if element.tag == "text": # possible to find vert files with more texts, account for that
                text = element
                for k,v in element.attrib.items():
                    vert_parsed["metadata_file"][k] = v

                for subelement in text:

                    if subelement.tag == "s":
                        sentence = subelement

                        sent_meta = sentence.attrib
                        for k in sent_meta:
                            if "id" in k:
                                sent_id = sent_meta[k]

                        vert_parsed["sentences"][sent_id] = {"sent_metadata": sent_meta, "sent_text": []}

                        sent_text = sentence.text.strip()
                        token_list = sent_text.split('\n')
                        for token in token_list:
                            form = token.split('\t')[0]
                            lemma = token.split('\t')[1]
                            pos = token.split('\t')[2]

                            token_dict = {"form": form, "lemma": lemma, "xpos": pos}

                            vert_parsed["sentences"][sent_id]["sent_text"].append(token_dict)
                    else:
                        print(subelement)
                        # for now processing only 's' elements. include 'p', 'title' and others
            else:
                print(element)
                # for now processing only 'text' elements

        return vert_parsed



def writer(input_dict, input_filename=None):

    vert_file_list = []

    vert_file_list.append("<corpus>\n")
    vert_file_list.append('<text id="{}">\n'.format(input_filename))

    for sent_id,sent_data in input_dict["sentences"].items():

        for item in sent_data:
            if "metadata" in item:
                sent_meta = sent_data[item]
            elif "text" in item:
                sent_text = sent_data[item]

        vert_file_list.append("<s")

        for k,v in sent_meta.items():
            kv_pair = ' {}="{}"'.format(k,v)
            vert_file_list.append(kv_pair)

        vert_file_list.append(">\n")


        for token in sent_text:
            token_list = [v for k,v in token.items()]
            token_str = "\t".join(token_list[1:4])
            vert_file_list.append(token_str+"\n")

        vert_file_list.append("</s>\n")

    vert_file_list.append('</text>\n')
    vert_file_list.append("</corpus>\n")

    return "".join(vert_file_list)

