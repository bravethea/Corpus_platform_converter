# Corpus format converter

The project for conversion of the basic corpus formats into one universal format as a part of the Corpus Platform within the LiRI Language Technology services. 
The purpose of the converter is to enable users to import corpora in one of the most common corpus formats and to upload it on the Corpus Platform and eventually use other services. 
The initialy supported input formats are TEI XML, CONLL, and the .vert CQP format. The output format is generated as JSON.

## Requirements
python 3.7

The module currently has no specific requirements.

## Input formats

The initialy supported input formats are TEI XML, CONLL, and the .vert CQP format. 

## Output formats

The intermediary output format is generated as JSON. The final output can be JSON or any of the input formats (conll, vert, xml)

## How to use

The tool is used from the command line, by adding path wiht a file name as arguments after flags.

Use flag `-in` or `-input_file` followed by a path for an input file, and flags `-out` or `-output_file` followed by a path for an output file, as in the example below:

`python converter.py -in input_file.conllu -out output_file.vert` 

## Corntributors

Teodora Vukovic and Danny McDonald (Langage Tech Team, LiRI, Univeristy of Zurich)
