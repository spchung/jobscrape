'''
scrape landing page for all job ids for later visit
'''
import sys
import os, re, json 

# Get the absolute path to the base directory
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir)


import time
from urllib.request import urlopen, Request
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
from data_model.models import JobMetaData
from typing import List
from controller.jobs import check_if_job_exists


def exec(
    search_term,
    page_limit,
    location,
    base_url = 'https://www.indeed.com/jobs',
    source = "indeed",
    per_page = 20        
) -> List[JobMetaData]:
    
    url = base_url + f"?q={search_term}" + f"&l={location}"
    
    # result
    job_metadata = []

    for start_index in range(0, page_limit * per_page, per_page):
        time.sleep(1)
        local_url =  url + f"&start={start_index}"
        encoded_url = quote(local_url, safe=':/?&=')
        request_site = Request(encoded_url, headers={"User-Agent": "Mozilla/5.0"})
        page = urlopen(request_site)
        html = page.read().decode("utf-8")
        soup = bs(html, "html.parser")
        
        print(f"[INFO] visiting url {encoded_url}")
        
        # per page
        job_results = soup.find("div", id="mosaic-provider-jobcards")
        

        list = job_results.find("ul")

        job_items = list.find_all("div", class_="cardOutline")
        for item in job_items:
            time.sleep(0.1)
            elem = bs(str(item), "html.parser")            

            company_name = ""
            company_location = elem.find("div", class_="company_location")
            if company_location:
                company_name_elem = company_location.find("span", {"data-testid":"company-name"})
                if company_name_elem:
                    company_name = company_name_elem.text

            job_title_h2 = elem.find("h2", class_="jobTitle")
            job_a = job_title_h2.find("a")
            
            attributes = job_a.attrs
            job_metadata.append(
                JobMetaData(
                    job_id = attributes.get("data-jk"),
                    company_id = None,
                    company = company_name,
                    title = job_a.text,
                    source = source
                )
            )
    return job_metadata