from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from tqdm import tqdm

import sys
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)

model = "en_core_web_lg"
# curr directory
output_dir = Path("model_outputs/m_software_engineer_job_ner")
n_iter=100

if model is not None:
    nlp = spacy.load(model)  
    print("Loaded model '%s'" % model)
else:
    nlp = spacy.blank('en')  
    print("Created blank 'en' model")

#set up the pipeline

if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe('ner', last=True)
else:
    ner = nlp.get_pipe('ner')

# treat annotation data'
import json
# open all files in training_data/annotations
training_data = []
for filename in Path("training_data/annotations").iterdir():
    if filename.suffix != ".json":
        continue
    print(filename)
    with open(filename) as f:
        data = json.load(f)
        text, annotations = data['annotations'][0]
        training_data.append((text, {"entities":annotations['entities']}))

for _, annotations in training_data:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

from spacy.training.example import Example

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):  # only train NER
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
        random.shuffle(training_data)
        losses = {}
        for batch in spacy.util.minibatch(training_data, size=2):
            for text, annotations in batch:
            # create Example
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                # Update the model
                nlp.update([example], losses=losses, drop=0.3)
        print(losses)

for text, _ in training_data:
    doc = nlp(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])

if output_dir is not None:
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir()
    nlp.to_disk(output_dir)
    print("Saved model to", output_dir)