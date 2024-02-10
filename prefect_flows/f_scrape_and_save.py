import sys
import os

# Get the absolute path to the base directory
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from phases.phase_one import phase_one
from phases.phase_two import phase_two
from phases.phase_three import phase_three
from config import config
from prefect import flow, task
from typing import List

'''
search_term = config.get('phase_one', 'search_terms')
    page_limit = config.get('phase_one', 'page_limit')
    base_url = config.get('phase_one', 'base_url')
    source = '1111'
'''

@task
def phase_one_task(
    search_term: str,
    page_limit: int,
    base_url: str,
    source: str
):
    # phase one
    # search_term = config.get('phase_one', 'search_terms')
    jobs_metadata_lis = phase_one.exec(
        search_term,
        page_limit,
        base_url,
        source
    )
    return jobs_metadata_lis

def phase_one_aysnc_wrapper(search_term, page_limit, base_url, source):
    jobs_metadata_lis = phase_one_task(search_term, page_limit, base_url, source)
    return jobs_metadata_lis

@task
def phase_two_task(jobs_metadata_lis: List[str]):
    # phase two
    job_ids = phase_two.exec(jobs_metadata_lis)
    return job_ids

def phase_two_async_wrapper(n, step, jobs_metadata_lis):
    workers = []
    for i in range(0, n, step):
        if i + step > n:
            small_lis = jobs_metadata_lis[i:]
        else:
            small_lis = jobs_metadata_lis[i:i+step]
        
        workers.append(phase_two_task.submit(small_lis)) # use submit for concurrency
    
    job_ids = []
    for worker in workers:
        job_ids += worker.result()
    return job_ids

@task
def phase_three_task(job_ids: List[str]):
    embedding_ids = phase_three.exec(job_ids)
    return embedding_ids

def phase_three_async_wrapper(n, step, job_ids):
    workers = []
    for i in range(0, n, step):
        if i + step > n:
            small_lis = job_ids[i:]
        else:
            small_lis = job_ids[i:i+step]
        
        workers.append(phase_three_task.submit(small_lis)) # use submit for concurrency
    
    embedding_ids = []
    for worker in workers:
        embedding_ids += worker.result()
    return embedding_ids

@flow(log_prints=True)
def scrape_and_embed(
        search_term: str, 
        base_url: str,
        source: str,
        page_limit: int = 5,
    ):
    jobs_metadata_lis = phase_one_task(
        search_term,
        page_limit,
        base_url,
        source
    )
    print(f"{len(jobs_metadata_lis)} new jobs discovered from - {source}")

    # concurrency:
    job_ids = phase_two_async_wrapper(len(jobs_metadata_lis), 20, jobs_metadata_lis)
    print(f"{len(job_ids)} jobs parsed and saved to database")


    embedding_ids = phase_three_async_wrapper(len(job_ids), 20, job_ids)
    print(f"{len(embedding_ids)} job embeddings generated and saved to database")

if __name__ == "__main__":
    scrape_and_embed(
        search_term=config.get('phase_one', 'search_terms'),
        base_url=config.get('phase_one', 'base_url'),
        page_limit=config.get('phase_one', 'page_limit'),
        source="1111",
    )
    