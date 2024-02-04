from database.models.embedding import SentenceEmbeddings
from embedding.helper import get_embedding
from data_model.models import Job
from database.connection import Session
from typing import List

def save_embedding(job: Job) -> None:
    session = Session()
    embedding = get_embedding(job.description)
    session.add(SentenceEmbeddings(text=job.description, embedding=embedding))
    session.commit()
    session.close()

def get_nearest_neighbors(search_embedding, limit=5) -> List[str]:
    session = Session()
    
    neighbors = session.query(
        SentenceEmbeddings
    ).order_by(
        SentenceEmbeddings.embedding.l2_distance(search_embedding)
    ).limit(limit).all()
    
    session.close()
    return [embedding.to_dict() for embedding in neighbors]