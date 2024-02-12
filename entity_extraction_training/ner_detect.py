# first we load the model
# import spacy

# # we create a document object and we test the fine-tuned model
# doc = nlp_ner("USA is a nation")

# # we print the entities
# spacy.displacy.render(doc, style="ent")

import spacy
nlp_ner = spacy.load("output/model-best")
# model = spacy.load("en_core_web_sm")

doc = nlp_ner('''Java and JavaScript are prominent in programming, with Java being renowned for its object-oriented approach and JavaScript for its versatility in web development. In the database realm, MS SQL, MySQL, and Oracle each have distinct advantages. MS SQL integrates seamlessly with Microsoft technologies, MySQL is favored for its scalability, and Oracle excels in enterprise-grade features. Combining Java or JavaScript with MS SQL, MySQL, or Oracle is common in software projects, creating powerful systems for data management and application development. Whether it's Java interfacing with Oracle for enterprise resources or JavaScript using MySQL for web app backend, these combinations drive innovation in tech.''')
ents = [(ent.text, ent.label_) for ent in doc.ents]
print(ents)