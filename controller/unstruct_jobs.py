from data_model.models import UnstructJob
from config import config
from database.connection import Session
from database.models.unstruct_jobs import UnstructJobs

def create_unstruct_job(job: UnstructJob):
    newJob = UnstructJobs.from_model(job)
    with Session() as session:
        session.add(newJob)
        session.commit()
        return newJob.job_id

def check_if_unstruct_job_exists(job_id: str) -> bool:
    session = Session()
    job = session.query(UnstructJobs).filter_by(job_id=job_id).first()
    session.close()
    return job is not None
