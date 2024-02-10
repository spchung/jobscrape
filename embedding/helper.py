from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
l12model = SentenceTransformer("all-MiniLM-L12-v2")

def get_embedding(text):
    return list(model.encode(text))
def get_embedding_l12(text):
    return list(l12model.encode(text))