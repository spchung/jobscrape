from pydantic import BaseModel

class JobMetaData(BaseModel):
    job_id: str
    company_id: str
    title: str

class Job(BaseModel):
    job_id: str 
    company_id: str
    title: str
    job_type: str | None
    location: str | None
    salary: str | None
    experience: str | None
    education_restriction: str | None
    subject_restriction: str | None
    work_skills: str | None
    technical_skills: str | None
    addition_requirements: str | None
    raw_html: str | None
    description: str | None
    last_updated: str | None