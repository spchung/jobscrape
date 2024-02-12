'''
uses the josn output from extract_en.py to imporove spacy NER
'''
import os
cwd = os.getcwd()
import json
training_data = []

# open all files in training_data/annotations
for filename in os.listdir("training_data/annotations"):
    with open("training_data/annotations/" + filename) as f:
        data = json.load(f)
        text, annotations = data['annotations'][0]

        training_data.append((text, annotations['entities']))

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
            print("success")
    doc.ents = ents
    db.add(doc)

# doc_bin.to_disk("train.spacy")
# save the docbin to disk
db.to_disk("entity_extraction_training/train.spacy")