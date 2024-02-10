from data_model.models import JobMinimal
from database.connection import Session
from database.models.jobs import Jobs as JobModel
from database.models.embedding import JobEmbeddingL12
from embedding.helper import get_embedding_l12
from sqlalchemy.sql import text

def get_all_jobs() -> list[JobMinimal]:
    with Session() as session:
        jobs = session.query(JobModel).all()
        return [
            JobMinimal(
                job_id=job.job_id,
                title=job.title,
                description=job.description)
            for job in jobs
        ]

def create_new_embedding_table():
    with Session() as session:
        statement = text("CREATE TABLE IF NOT EXISTS job_embeddings_l12 (job_id varchar PRIMARY KEY, title_emb vector(384), description_emb vector(384))")
        session.execute(statement)
        session.commit()

def embed_and_save(lis: list[JobMinimal]):
    embedding_ids = []
    with Session() as session:
        for job in lis:
            job_embedding = JobEmbeddingL12(
                job_id=job.job_id,
                title_emb=get_embedding_l12(job.title),
                description_emb=get_embedding_l12(job.description)
            )
            session.add(job_embedding)
            embedding_ids.append(job_embedding.job_id)
        session.commit()
    return embedding_ids
    