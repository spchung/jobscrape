from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, String, Integer

from database.connection import Base
from sqlalchemy.orm import mapped_column
from data_model.models import JobEmbedding

class SentenceEmbeddings(Base):
    __tablename__ = "sentence_embeddings"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    embedding = embedding = mapped_column(Vector(384))

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "embedding": self.embedding
        }
# using all-MiniLM-L6-v2
class JobEmbedding(Base):
    __tablename__ = "job_embeddings"
    job_id = Column(String, primary_key=True, index=True)
    title_emb = Column(Vector(384))
    description_emb = Column(Vector(384))

    def to_dict(self):
        return {
            "job_id": self.job_id,
            "title_emb": self.title_emb,
            "description_emb": self.description_emb
        }
    
    def from_job_embedding(job_embedding: JobEmbedding):
        return JobEmbedding(
            job_id=job_embedding.job_id,
            title_emb=job_embedding.title_emb,
            description_emb=job_embedding.description_emb
        )

# using all-MiniLM-L12-v2
class JobEmbeddingL12(Base):
    __tablename__ = "job_embeddings_l12"
    job_id = Column(String, primary_key=True, index=True)
    title_emb = Column(Vector(384))
    description_emb = Column(Vector(384))

    def to_dict(self):
        return {
            "job_id": self.job_id,
            "title_emb": self.title_emb,
            "description_emb": self.description_emb
        }
    
    def from_job_embedding(job_embedding: JobEmbedding):
        return JobEmbedding(
            job_id=job_embedding.job_id,
            title_emb=job_embedding.title_emb,
            description_emb=job_embedding.description_emb
        )
