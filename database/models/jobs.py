
from sqlalchemy import Column, String
from data_model.models import Job

from database.connection import Base

class Jobs(Base):
    __tablename__ = "jobs"
    job_id = Column(String, primary_key=True, index=True)
    company_id = Column(String)
    title = Column(String)
    job_type = Column(String)
    location = Column(String)
    salary = Column(String)
    experience = Column(String)
    education_restriction = Column(String)
    subject_restriction = Column(String)
    work_skills = Column(String)
    technical_skills = Column(String)
    addition_requirements = Column(String)
    raw_html = Column(String)
    description = Column(String)
    last_updated = Column(String)
    url = Column(String)
    source = Column(String)

    def from_job_model(job: Job):
        return Jobs(
            job_id=job.job_id,
            company_id=job.company_id,
            title=job.title,
            job_type=job.job_type,
            location=job.location,
            salary=job.salary,
            experience=job.experience,
            education_restriction=job.education_restriction,
            subject_restriction=job.subject_restriction,
            work_skills=job.work_skills,
            technical_skills=job.technical_skills,
            addition_requirements=job.addition_requirements,
            raw_html=job.raw_html,
            description=job.description,
            last_updated=job.last_updated,
            url=job.url,
            source=job.source
        )
    
    def to_job_model(self) -> Job:
        return Job(
            job_id=self.job_id,
            company_id=self.company_id,
            title=self.title,
            job_type=self.job_type,
            location=self.location,
            salary=self.salary,
            experience=self.experience,
            education_restriction=self.education_restriction,
            subject_restriction=self.subject_restriction,
            work_skills=self.work_skills,
            technical_skills=self.technical_skills,
            addition_requirements=self.addition_requirements,
            raw_html=self.raw_html,
            description=self.description,
            last_updated=self.last_updated,
            url=self.url,
            source=self.source
        )
