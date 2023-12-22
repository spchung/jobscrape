from phase_one import phase_one
from phase_two import phase_two
import configparser

def main():
    # phase one
    config = configparser.ConfigParser()
    config.read('config.cfg')
    search_term = config.get('phase_one', 'search_terms')
    page_limit = config.get('phase_one', 'page_limit')
    base_url = config.get('phase_one', 'base_url')
    jobs_metadata_lis = phase_one.exec(
        search_term,
        page_limit,
        base_url
    )
    
    small_lis = jobs_metadata_lis[:1]
    jobs = phase_two.exec(small_lis)
    print(jobs)

if __name__ == "__main__":
    main()