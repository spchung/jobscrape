from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, String, Integer

from database.connection import Base
from sqlalchemy.orm import mapped_column

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
