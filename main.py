from phases.phase_one import phase_one
from phases.phase_two import phase_two
from config import config

def main():
    # phase one
    search_term = config.get('phase_one', 'search_terms')
    page_limit = config.get('phase_one', 'page_limit')
    base_url = config.get('phase_one', 'base_url')
    jobs_metadata_lis = phase_one.exec(
        search_term,
        page_limit,
        base_url
    )
    
    small_lis = jobs_metadata_lis[:5]
    jobs = phase_two.exec(small_lis)
    print(jobs)

if __name__ == "__main__":
    main()