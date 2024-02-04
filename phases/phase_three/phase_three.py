'''
Perform embedding on job data

1. embed job title and description
'''
from data_model.models import JobEmbedding
from embedding.helper import get_embedding
from controller.jobs import get_jobs_by_ids
from controller.embeddings import save_job_embedding
from typing import List

def exec(
    job_ids: List[str]
) -> JobEmbedding:
    job_embeddings = []
    jobs = get_jobs_by_ids(job_ids)
    for job in jobs:
        job_embeddings.append(JobEmbedding(
            job_id=job.job_id,
            title_emb=get_embedding(job.title),
            description_emb=get_embedding(job.description)
        ))

    # save to database
    embedding_ids = []
    for job_embedding in job_embeddings:
        embedding_id = save_job_embedding(job_embedding)
        embedding_ids.append(embedding_id)
    
    return embedding_ids