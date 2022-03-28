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
input_path = "output_files/json_out.json"

def writer(input_dict):

    vert_file_list = []

    vert_file_list.append("<corpus>\n")
    vert_file_list.append('<text id="lll">\n')

    for sent_id,sent_text in input_dict["sentences"].items():
        vert_file_list.append("<s>\n")

        for token in sent_text:
            token_str = "\t".join(token[1:4])

            vert_file_list.append(token_str+"\n")
        vert_file_list.append("</s>\n")

    vert_file_list.append("</corpus>\n")
    vert_file_list.append('</text>\n')

    return "".join(vert_file_list)



        # print(json_object)

# if __name__ == "__main__":
#     writer(input_path)

