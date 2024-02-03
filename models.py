from pydantic import BaseModel

class JobMetaData(BaseModel):
    job_id: str
    company_id: str
    title: str

class Job(BaseModel):
    job_id: str
    company_id: str
    title: str
    job_type: str
    location: str
    salary: str
    experience: str
    education_restriction: str
    subject_restriction: str
    work_skills: str
    technical_skills: str
    addition_requirements: str
    raw_html: str
    description: str