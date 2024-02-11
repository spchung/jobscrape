from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobMetaData(BaseModel):
    job_id: str
    company_id: str | None
    title: str
    source: str 

class Job(BaseModel):
    job_id: str 
    company_id: str
    title: str
    url: str
    source: str
    job_type: Optional[str | None]
    location: Optional[str | None]
    salary: Optional[str | None]
    experience: Optional[str | None]
    education_restriction: Optional[str | None]
    subject_restriction: Optional[str | None]
    work_skills: Optional[str | None]
    technical_skills: Optional[str | None]
    addition_requirements: Optional[str | None]
    raw_html: Optional[str | None]
    description: Optional[str | None]
    last_updated: Optional[str | None]

class JobMinimal(BaseModel):
    job_id: str
    title: str
    description: str

class JobEmbedding(BaseModel):
    job_id: str
    description_emb: list[float]
    title_emb: list[float]

class UnstructJob(BaseModel):
    job_id: str
    source: str
    title: str
    location: str
    description_blob: str
    url: str
    scrapped_at: datetime