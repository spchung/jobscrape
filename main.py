from phases.phase_one import phase_one
from phases.phase_two import phase_two
from phases.phase_three import phase_three
from config import config

def main():
    search_term = config.get('phase_one', 'search_terms')
    page_limit = config.get('phase_one', 'page_limit')
    base_url = config.get('phase_one', 'base_url')
    source = '1111'
    
    # phase one
    jobs_metadata_lis = phase_one.exec(
        search_term,
        page_limit,
        base_url,
        source
    )
    
    # phase two
    small_lis = jobs_metadata_lis
    job_ids = phase_two.exec(small_lis)

    # phase three - generate embeddings
    embedding_ids = phase_three.exec(job_ids)


if __name__ == "__main__":
    main()