import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)

from prefect import flow, task
from jobs.regen_embedding import get_all_jobs, create_new_embedding_table, embed_and_save
from data_model.models import JobMinimal

@task
def get_jobs() -> list[JobMinimal]:
    return get_all_jobs()

@task
def create_new_embedding_table_task():
    return create_new_embedding_table()

@task
def embed_and_save_task(miniList: list[JobMinimal]):
    return embed_and_save(miniList)

def embed_and_save_task_wrapper(step, jobs: list[JobMinimal]):
    workers = []
    for i in range(0, len(jobs), step):
        if i + step > len(jobs):
            small_lis = jobs[i:]
        else:
            small_lis = jobs[i:i+step]
        
        workers.append(embed_and_save_task.submit(small_lis))
    
    embedding_ids = []
    for worker in workers:
        embedding_ids += worker.result()
    return embedding_ids
    
@flow(log_prints=True)
def generate_embedding():
    jobs_mini = get_jobs()
    create_new_embedding_table_task()
    return embed_and_save_task_wrapper(10, jobs_mini)
    
if __name__ == '__main__':
    generate_embedding()