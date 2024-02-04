import time
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
from data_model.models import JobMetaData
from typing import List
from controller.jobs import check_if_job_exists

'''
    inputs:
    - search term
    - page limit (15 default)
    - sort (desc)
'''

def exec(
    search_term,
    page_limit,
    base_url
) -> List[JobMetaData]:
    curr_page = 1
    jobs = []
    page_limit = int(page_limit)
    while curr_page <= page_limit:
        time.sleep(1)
        url = base_url + f"?ks={search_term}&page={curr_page}&sort=desc"
        encoded_url = quote(url, safe=':/?&=')
        page = urlopen(encoded_url)
        html = page.read().decode("utf-8")
        soup = bs(html, "html.parser")

        print(f"[INFO] visiting url {url}")
        # per page
        job_items = soup.find_all("div", class_="item__job job_item")

        for item in job_items:
            time.sleep(0.1)
            elem = bs(str(item), "html.parser")
            job_info = elem.find("div", class_="job_item_info")

            a_elem = job_info.find_all("a") ## job link, company link
            job_link_elem = a_elem[0]
            company_link_elem = a_elem[1]

            # job id
            job_link = job_link_elem["href"]
            link_split = job_link.split("/")
            job_id = link_split[-2]

            ## check job id exists
            if check_if_job_exists(job_id):
                print(f"[INFO] job id {job_id} exists, skipping")
                continue

            # company id    
            company_link = company_link_elem["href"]
            link_split = company_link.split("/")
            company_id = link_split[-2]

            # job title
            title = job_link_elem.text

            job = JobMetaData(job_id=job_id, company_id=company_id, title=title)
            
            jobs.append(job)
        
        curr_page += 1
    return jobs
    