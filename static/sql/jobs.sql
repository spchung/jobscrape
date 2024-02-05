-- -------------------------------------------------------------
-- TablePlus 5.3.8(500)
--
-- https://tableplus.com/
--
-- Database: postgres
-- Generation Time: 2024-02-05 14:26:00.0730
-- -------------------------------------------------------------


DROP TABLE IF EXISTS "public"."jobs";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."jobs" (
    "job_id" varchar NOT NULL,
    "company_id" varchar,
    "title" varchar,
    "job_type" varchar,
    "location" varchar,
    "salary" varchar,
    "experience" varchar,
    "education_restriction" varchar,
    "subject_restriction" varchar,
    "work_skills" varchar,
    "technical_skills" varchar,
    "addition_requirements" varchar,
    "raw_html" varchar,
    "description" varchar,
    "last_updated" varchar,
    "url" varchar,
    "source" varchar,
    PRIMARY KEY ("job_id")
);

