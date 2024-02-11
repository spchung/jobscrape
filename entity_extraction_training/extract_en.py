import sys
import os, json

# Get the absolute path to the base directory
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir)

import spacy
from spacy.training import Example, offsets_to_biluo_tags
import random
from pprint import pprint

from controller.jobs import query_jobs, get_job_by_id


def extract(text: str, seperator = '|'):
    words = text.split(seperator)
    start_i = 0
    end_i = 0

    for word in words:
        end_i = start_i + len(word)
        yield (start_i, end_i, word)
        start_i = end_i + 1

jobs = query_jobs()

skills_per_job = []
for job in jobs:
    skills = []
    
    skills += job.work_skills.split("|")
    skills += job.technical_skills.split("|")
    skills = [skill for skill in skills if skill.strip() != "" and skill.isascii()]

    skills = "|".join(skills)
    if skills != "":
        skills_per_job.append(skills)

# ## generate a context object for every 30 jobs

step = 30
result = []
for i in range(0, len(skills_per_job), step):
    if i + step > len(skills_per_job):
        chunks_job_skills = skills_per_job[i:]
    else:
        chunks_job_skills = skills_per_job[i:i+step]
    
    set_of_skills = set() # global skills set
    
    # every n jobs
    entities = []
    for job_skills in chunks_job_skills:
        for ent in extract(job_skills):
            start, end, skill_name = ent # start and end index of the skill
            if skill_name and skill_name not in set_of_skills:
                set_of_skills.add(skill_name)
                entities.append({
                    "start": start,
                    "end": end-1,
                    "label": "SKILL"
                })

    result.append({
        "context": "|".join(chunks_job_skills),
        "annotations": entities
    })

json.dump(result, open("skills.json", "w"), indent=4)

