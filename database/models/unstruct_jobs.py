from sqlalchemy import Column, String, Text, Time
from data_model.models import Job, UnstructJob as UnstructJobModel

from database.connection import Base

class UnstructJobs(Base):
    __tablename__ = "unstruct_jobs"
    job_id = Column(String, primary_key=True, index=True)
    source = Column(String)
    title = Column(String)
    location = Column(String)
    url = Column(String)
    description_blob = Column(Text)
    scrapped_dt = Column(Time)

    def from_model(job: UnstructJobModel):
        return UnstructJobs(
            job_id=job.job_id,
            source=job.source,
            title=job.title,
            location=job.location,
            url=job.url,
            description_blob=job.description_blob,
            scrapped_dt=job.scrapped_at
        )
    
    def to_model(self) -> UnstructJobModel:
        return UnstructJobModel(
            job_id=self.job_id,
            source=self.source,
            title=self.title,
            location=self.location,
            url=self.url,
            description_blob=self.description_blob,
            scrapped_at=self.scrapped_dt
        )
    