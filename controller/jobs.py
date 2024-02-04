# crud on jobs table
from data_model.models import Job
from config import config
from database.connection import Session
from database.models.jobs import Jobs as JobModel

def create_job(job: Job):
    newJob = JobModel.from_job_model(job)
    session = Session()
    session.add(newJob)
    session.commit()
    session.close()

def get_job_by_id(job_id: str) -> Job:
    session = Session()
    job = session.query(JobModel).filter_by(job_id=job_id).first()
    session.close()
    if job is None:
        return None
    return Job(
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
        description=job.description
    )

def check_if_job_exists(job_id: str) -> bool:
    session = Session()
    job = session.query(JobModel).filter_by(job_id=job_id).first()
    session.close()
    return job is not None