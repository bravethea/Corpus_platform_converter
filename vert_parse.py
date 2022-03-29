import codecs
import re
import json

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
        sentences = [sent for sent in input_data.split('\n\n') if sent]

        conllu_parsed = {
            "metadata_file": {},
            "sentences": {}
        }

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
            kv_pair = " {}={}".format(k,v)
            vert_file_list.append(kv_pair)

        vert_file_list.append(">\n")


        for token in sent_text:
            token_list = [v for k,v in token.items()]
            token_str = "\t".join(token_list[1:4])
            vert_file_list.append(token_str+"\n")

        vert_file_list.append("</s>\n")

    vert_file_list.append("</corpus>\n")
    vert_file_list.append('</text>\n')

    return "".join(vert_file_list)

