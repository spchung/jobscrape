import spacy 
output_dir = "model_outputs/m_software_engineer_job_ner"
print("Loading from", output_dir)
nlp2 = spacy.load(output_dir)
from pathlib import Path

text = '''

We are looking for a Software Engineer to join our growing Engineering team and build out the next generation of our platform. The ideal candidate is a hands-on platform builder with significant experience in developing scalable data platforms. We're looking for someone with experience in business intelligence, analytics, data science and data products. They must have strong, firsthand technical expertise in a variety of configuration management and big data technologies and the proven ability to fashion robust scalable solutions that can manage large data sets. They must be at ease working in an agile environment with little supervision. This person should embody a passion for continuous improvement and test-driven development.

'''
doc = nlp2(text)
for ent in doc.ents:
    print(ent.text, ent.label_)