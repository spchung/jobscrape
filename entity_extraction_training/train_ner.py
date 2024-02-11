'''
uses the josn output from extract_en.py to imporove spacy NER
'''
import os
cwd = os.getcwd()
import json
training_data = []

with open('skills.json', 'r') as f:
    data = json.load(f)
    for chunk in data:
        
        annotations = []
        for anno in chunk['annotations']:
            annotations.append((anno['start'], anno['end'], anno['label']))

        training_data.append(
            (chunk['context'], annotations)
        )

from spacy.tokens import DocBin
import spacy 

nlp = spacy.blank('en')
db = DocBin()
for text, annotations in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations:
        span = doc.char_span(start, end, label=label)
        if span is None:
            print("Skipping entity")
            pass
        else:
            ents.append(span)
    doc.ents = ents
    db.add(doc)

# doc_bin.to_disk("train.spacy")
# save the docbin to disk
db.to_disk("entity_extraction_training/train.spacy")