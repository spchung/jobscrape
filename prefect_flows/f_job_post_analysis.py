'''
This flow runs job posting through NLP pipeline and extracts entities
Then run embedding on EXPERIENECE entities and save to vector DB
Then save SKILLS entities to graph DB
'''

'''
- Trigger:
  - CRON
- Target:
  - Any row in table 'unstruct_job' that has column 'analyzed' set to False
- Flow:
  - Get unstruct job
  - Run NLP pipeline
  - Extract entities
  - Save to vector DB
  - Save to graph DB
'''
from neo4j_database import get_driver
from database.connection import Session
from database.models.unstruct_jobs import UnstructJobs
from prefect import task, Flow
from typing import List
from controller.jobs import create_job_neo4j_entity, create_require_skill_relationship

# step 1: get unstruct job
@task
def get_unanalyzed_jobs():
  with Session() as session:
    unanalyzed_jobs = session.query(UnstructJobs).filter_by(analyzed=False).all()
  return unanalyzed_jobs

# step 2: run NLP pipeline
@task
def run_nlp_batch(jobs: List[UnstructJobs]):
  res = []
  for job in jobs:
    # TODO: run NLP pipeline
    pass
  return res

def nlp_batch_wrapper(n, step, jobs):
  workers = []
  for i in range(0, n, step):
    if i + step > n:
        small_lis = jobs[i:]
    else:
        small_lis = jobs[i:i+step]
    
    workers.append(run_nlp_batch.submit(small_lis)) # use submit for concurrency
    
  job_ids = []
  for worker in workers:
      job_ids += worker.result()
  return job_ids

# step 3: save to neo4j
@task
def save_to_neo4j(jobs: List[UnstructJobs]):
  driver = get_driver()
  for job in jobs:
    driver.execute_query(f"""
      CREATE (job:Job {{
        job_id: "{job.job_id}",
        title: "{job.title}",
        location: "{job.location}",
        company: "{job.company}",
        url: "{job.url}"
      }})
    """)