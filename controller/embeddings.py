from database.models.embedding import SentenceEmbeddings, JobEmbedding as JobEmbeddingModel
from embedding.helper import get_embedding
from data_model.models import Job, JobEmbedding
from database.connection import Session
from typing import List

def save_embedding(job: Job) -> None:
    with Session() as session:
        embedding = get_embedding(job.description)
        new_embedding = SentenceEmbeddings(
            sentence=job.description,
            embedding=embedding
        )
        session.add(new_embedding)
        session.commit()
        return new_embedding.id

def save_job_embedding(job_embedding: JobEmbedding) -> None:
    with Session() as session:
        new_job_embedding = JobEmbeddingModel(
            job_id=job_embedding.job_id,
            title_emb=job_embedding.title_emb,
            description_emb=job_embedding.description_emb
        )
        session.add(new_job_embedding)
        session.commit()
        return new_job_embedding.job_id
        

def get_nearest_neighbors(search_embedding, limit=5) -> List[str]:
    session = Session()
    
    neighbors = session.query(
        SentenceEmbeddings
    ).order_by(
        SentenceEmbeddings.embedding.l2_distance(search_embedding)
    ).limit(limit).all()
    
    session.close()
    return [embedding.to_dict() for embedding in neighbors]