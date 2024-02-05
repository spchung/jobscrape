-- -------------------------------------------------------------
-- TablePlus 5.3.8(500)
--
-- https://tableplus.com/
--
-- Database: postgres
-- Generation Time: 2024-02-05 14:25:46.6740
-- -------------------------------------------------------------


DROP TABLE IF EXISTS "public"."job_embeddings";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."job_embeddings" (
    "job_id" varchar NOT NULL,
    "title_emb" vector,
    "description_emb" vector,
    PRIMARY KEY ("job_id")
);

