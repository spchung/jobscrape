# crud on jobs table
from data_model.models import JobMinimal, Job
from config import config
from database.connection import Session
from database.models.jobs import Jobs as JobModel

def create_job(job: Job):
    newJob = JobModel.from_job_model(job)
    with Session() as session:
        session.add(newJob)
        session.commit()
        return newJob.job_id

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

def get_jobs_by_ids(job_ids: list[str]) -> list[Job]:
    with Session() as session:
        jobs = session.query(JobModel).filter(JobModel.job_id.in_(job_ids)).all()
        return [
            JobMinimal(
                job_id=job.job_id,
                title=job.title,
                description=job.description)
            for job in jobs
        ]

def check_if_job_exists(job_id: str) -> bool:
    session = Session()
    job = session.query(JobModel).filter_by(job_id=job_id).first()
    session.close()
    return job is not None

def query_jobs(
    company_id: str,
    title: str,
    job_type: str,
    location: str,
    salary: str,
    experience: str,
    education_restriction: str,
    subject_restriction: str,
    work_skills: str,
    technical_skills: str,
    addition_requirements: str
) -> list[JobMinimal]:
    with Session() as session:
        query = session.query(JobModel)
        if company_id:
            query = query.filter_by(company_id=company_id)
        if title:
            query = query.filter(JobModel.title.like(f"%{title}%"))
        if job_type:
            # like 
            query = query.filter(JobModel.job_type.like(f"%{job_type}%"))
        if location:
            query = query.filter(JobModel.location.like(f"%{location}%"))
        if salary:
            query = query.filter(JobModel.salary.like(f"%{salary}%"))
        if experience:
            query = query.filter(JobModel.experience.like(f"%{experience}%"))
        if education_restriction:
            query = query.filter(JobModel.education_restriction.like(f"%{education_restriction}%"))
        if subject_restriction:
            query = query.filter(JobModel.subject_restriction.like(f"%{subject_restriction}%"))
        if work_skills:
            query = query.filter(JobModel.work_skills.like(f"%{work_skills}%"))
        if technical_skills:
            query = query.filter(JobModel.technical_skills.like(f"%{technical_skills}%"))
        if addition_requirements:
            query = query.filter(JobModel.addition_requirements.like(f"%{addition_requirements}%"))
        jobs = query.all()
        return [
            JobMinimal(
                job_id=job.job_id,
                title=job.title,
                description=job.description)
            for job in jobs
        ]
        
        