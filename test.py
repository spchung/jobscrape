from web_scrapper.indeed import get_jobs_meta, get_job_content

lis = get_jobs_meta.exec('software engineer', 1, 'new york')

get_job_content.exec('software engineer', 'new york', lis)