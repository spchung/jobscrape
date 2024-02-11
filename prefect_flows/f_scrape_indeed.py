import sys, os
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)

from config import config
from prefect import flow, task
from typing import List
from web_scrapper.indeed.get_jobs_meta import exec as get_jobs_meta
from web_scrapper.indeed.get_job_content import exec as get_job_content
from data_model.models import JobMetaData

'''
This work flow collects raw description text from indeed.com

This flow will not generate embeddings for the job descriptions.

This flow is purely for data collection for late NLP model training use.

Goal is to generate a model that can use information from the `unstruct_jobs` fill in the `jobs` table.
'''

@task
def get_jobs_meta_task(
    search_term: str,
    page_limit: int,
    location: str
) -> List[JobMetaData]:
    return get_jobs_meta(search_term, page_limit, location)

@task
def get_job_content_task(
    search_term: str,
    location: str,
    job_metadata_lis: List[str]
) -> List[str]:
    return get_job_content(search_term, location, job_metadata_lis)

def get_job_content_async_wrapper(n, step, search_term, location, job_metadata_lis):
    workers = []
    for i in range(0, n, step):
        if i + step > n:
            small_lis = job_metadata_lis[i:]
        else:
            small_lis = job_metadata_lis[i:i+step]
        
        workers.append(get_job_content_task.submit(search_term, location, small_lis)) # use submit for concurrency
    
    job_ids = []
    for worker in workers:
        job_ids += worker.result()

    return job_ids

@flow(name="scrape_indeed", log_prints=True)
def scrape_indeed_flow(
    search_term: str,
    page_limit: int,
    location: str
):
    job_metadata_lis = get_jobs_meta_task(search_term, page_limit, location)
    print(f"len: {len(job_metadata_lis)}")

    job_ids = get_job_content_async_wrapper(len(job_metadata_lis), 10, search_term, location, job_metadata_lis)
    print(f"len new jobs: {len(job_ids)}")

    return job_ids


if __name__ == "__main__":
    scrape_indeed_flow(
        search_term=config.get('indeed', 'search_terms'),
        location=config.get('indeed', 'location'),
        page_limit=config.get('indeed', 'page_limit'),
    )
    