from typing import List
from models import JobMetaData, Job
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from typing import Tuple
from database.connection import Session
from database.models import SentenceEmbedding
from embedding.helper import get_embedding

'''
    inputs:
    - search term
    - page limit (15 default)
    - sort (desc)
'''
def clean_list_field(field: str) -> str:
    field = field.replace("\r", "")
    field = field.split("\n")
    sub = [s.strip() for s in field]
    return "|".join([s for s in sub if s != ""])

def clean_text_field(field: str) -> str:
    field = field.replace("\r", "")
    field = field.replace("\n", " ")
    return field.strip()

def get_exact_match_field(soup: bs, field: str, elem:str='span') -> Tuple[str, str]:
    matching_element = soup.find(elem, string=field)

    value = ""
    if matching_element:
        value = matching_element.parent.find("span", class_="job_info_content").text
    return (field, value)

def parse_job_page(meta: JobMetaData) -> Job:
    job_id = meta.job_id

    url = f"https://www.1111.com.tw/job/{job_id}/"
    print(f"[INFO] visiting {url}")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = bs(html, "html.parser")
            
    # type
    job_type = soup.find("div", class_="ui_items job_type").text

    # job_salary
    salary = soup.find("div", class_="ui_items job_salary").text

    # job_location
    location = soup.find("div", class_="ui_items job_location").text

    # description
    description_group = soup.find("div", class_="body_2 description_info")
    lines = description_group.find_all("p")
    description = '\n'.join([line.text for line in lines])

    # - 工作經驗
    _, work_exp = get_exact_match_field(soup, "工作經驗：")
    # - 學歷限制
    _, education_limit = get_exact_match_field(soup, "學歷限制：")
    # - 科系限制
    _, department_limit = get_exact_match_field(soup, "科系限制：")
    # - 工作技能
    _, skill = get_exact_match_field(soup, "工作技能：")
    # - 電腦專長
    _, computer_skill = get_exact_match_field(soup, "電腦專長：")
    # - 附加條件
    matching_element = soup.find("div", string="附加條件：")
    additional = matching_element.parent.find("div", class_="ui_items_group").text

    job = Job(
        job_id=job_id,
        company_id=meta.company_id,
        title=meta.title,
        job_type=clean_text_field(job_type),
        location=clean_text_field(location),
        salary=clean_text_field(salary),
        experience=clean_text_field(work_exp),
        education_restriction=clean_text_field(education_limit),
        subject_restriction=clean_text_field(department_limit),
        work_skills=clean_list_field(skill),
        technical_skills=clean_list_field(computer_skill),
        addition_requirements=clean_list_field(additional),
        raw_html="",
        description=description
    )
    return job

def save_embedding(job: Job) -> None:
    session = Session()
    embedding = get_embedding(job.description)
    session.add(SentenceEmbedding(text=job.description, embedding=embedding))
    session.commit()
    session.close()
    

def exec(job_metadata_lis: List[JobMetaData]) -> List[JobMetaData]:
    # visit each page and then parse info
    jobs = []
    for meta in job_metadata_lis:
        try:
            job = parse_job_page(meta)

            # for description in job

            # save_embedding(job)
            save_embedding(job)
            
        except Exception as e:
            print(f"[ERROR] {e}")
    return jobs
        



