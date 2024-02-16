import spacy 
output_dir = "model_outputs/m_software_engineer_job_ner"
print("Loading from", output_dir)
nlp2 = spacy.load(output_dir)
from pathlib import Path

text = '''


Experience in C/C++ development required.
'''
doc = nlp2(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
print("done")