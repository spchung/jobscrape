
from controller.jobs import create_job
from controller.embeddings import get_nearest_neighbors
from embedding.helper import get_embedding

embedding = get_embedding("智能系統開發")
jobs = get_nearest_neighbors(embedding, 5)

for job in jobs:
    print(job['id'], job['text'])