from bs4 import BeautifulSoup as bs
from data_model.models import JobMetaData
from urllib.request import urlopen, Request
from typing import List
import time
from datetime import datetime
from data_model.models import UnstructJob as UnstructJobModel
from controller.unstruct_jobs import create_unstruct_job, check_if_unstruct_job_exists

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def visit_page_v2(base_url: str, meta: JobMetaData):

    url = base_url + f"&vjk={meta.job_id}"
    # Configure Selenium
    driver = webdriver.Chrome()  # You'll need to download the appropriate driver for your browser
    driver.get(url)

    # Wait for certain elements to load
    timeout = 10  # Maximum time to wait in seconds
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)  # Let the page load a second
    except Exception:
        print("Timed out waiting for page to load")

    # Get the page source
    page_source = driver.page_source

    # Pass the page source to Beautiful Soup for parsing
    soup = BeautifulSoup(page_source, 'html.parser')
    return url, soup

def visit_job_page(base_url: str, meta: JobMetaData) -> bs:
    url = base_url + f"&vjk={meta.job_id}"
    # encoded_url = quote(url, safe=':/?&=')
    request_site = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
    page = urlopen(request_site)
    
    print(f"[INFO] visiting {url}")

    html = page.read().decode("utf-8")
    soup = bs(html, "html.parser")
    return soup

def scrape_job_content(
        page_soup: bs, 
        url: str, 
        meta: JobMetaData,
        search_term: str,
        search_location: str
    ) -> UnstructJobModel:

    right_pane = page_soup.find("div", class_="jobsearch-RightPane")

    # location
    location = ""
    job_header = right_pane.find("div", class_="jobsearch-CompanyInfoWithoutHeaderImage")
    if job_header:
        elem = job_header.find("div", {"data-testid":"inlineHeader-companyLocation"})
        if elem:
            location = elem.text

    # description
    description_blob = right_pane.find("div", id="jobDescriptionText")
    if description_blob:
        description_blob = description_blob.text
    
    if not description_blob:
        return None

    return UnstructJobModel(
        job_id = meta.job_id,
        source = meta.source,
        company = meta.company,
        title = meta.title,
        location = location,
        description_blob = description_blob,
        url = url,
        scrapped_at = datetime.utcnow(),
        search_term = search_term,
        search_location = search_location
    )
    

def exec(
    search_term,
    location,
    job_metadata_lis: List[JobMetaData]
) -> List[JobMetaData]:
    
    search_term = search_term.replace(" ", "+")
    location = location.replace(" ", "+")

    base_url = f'https://www.indeed.com/jobs?q={search_term}&l={location}'
    job_ids = []
    for meta in job_metadata_lis:

        # if exist skip
        if check_if_unstruct_job_exists(meta.job_id):
            print(f"[INFO] job id {meta.job_id} exists in database, skipping")
            continue

        url, page_soup = visit_page_v2(base_url, meta)
        
        unstruct_job_model = scrape_job_content(page_soup, url, meta, search_term, location)
        if unstruct_job_model:
            try:
                new_id = create_unstruct_job(unstruct_job_model)
            except Exception as e:
                print(f"[ERROR] failed to create unstruct job {meta.job_id} with error: {e}")
                continue
        if new_id:
            job_ids.append(new_id)
    
    return job_ids



