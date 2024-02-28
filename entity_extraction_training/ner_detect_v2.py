import spacy 
output_dir = "model_outputs/m_software_engineer_job_ner"
print("Loading from", output_dir)
nlp2 = spacy.load(output_dir)
from pathlib import Path

text = '''


  Thank you for considering Progyny!
 




     As a Senior Software Engineer, you will work with a cross functional team of Database, DevOps, Salesforce, Software, QA engineers, Product and Project Management to develop solutions for critical projects. You will implement solutions, assist in defining scope and sizing of work, lead projects and other engineers at times, participate in technical discovery of new projects, and collaborate with other teammates to brainstorm ideas and review solutions and code that follows best practices.
   




     Responsibilities:
   





       Implement code that follows best practices based on technical specifications for projects.
     


       Assist and lead solution architecture for in-house development efforts, integrations with third party services, and designing/developing complex features for stakeholder needs.
     


       Research, recommend, and test modern technology stacks and tools to meet technology and project goals and help the Engineering team migrate toward their use.
     


       Participate in technical discovery phase of program development lifecycle in researching technologies and creating proof of concepts to present as potential solutions.
     


       Occasionally lead and manage projects from the technical side.
     


       Work with application developers, users, operational leadership, and subject matter experts to understand current and future operational goals.
     


       Review existing solutions, projects, and infrastructure to provide recommendations for enhancements and structural improvements.
     


       Provide feedback to fellow engineers during code reviews, brainstorming sessions, and technical discovery work.
     


       Help develop a distributed system with concurrent access and usage patterns.
     


       Help advance and optimize software development lifecycle with development, QA/testing, and deployment.
     


       Work closely with our product team to understand the needs of our clients.
     





     Required Skills and Experience:
   





       Bachelor's Degree in Computer Science, Engineering or related field, or equivalent experience.
     


       5+ years experience in Software Engineering utilizing one or more programming languages
     


       3+ years experience being a technical lead on projects, researching and presenting technical solutions
     


       Extensive experience with SQL and either MySQL or similar relational database systems (MariaDB, PostgreSQL)
     








       Detailed working knowledge of REST API development and supporting tools (e.g. Postman)
     


       Extensive experience with Docker and AWS or similar cloud services
     


       Extensive experience in implementation methodologies, software development lifecycle process, and project management
     


       Extensive experience with software project planning and organization with strong problem solving and communication skills
     


       Detailed working knowledge of AWS serverless services (AWS Lambda, S3, Aurora) and how to evaluate serverless vs. traditional services (EC2, ECS on EC2, etc.)
     


       Extensive knowledge of ETL development and supporting tools (ETL Tools such as Fivetran, Jitterbit, AWS Step Functions, Apache Airflow, etc.)
     


       Detailed knowledge of advanced workflow development (schedule vs. event-based jobs, queued jobs, jobs that depend on other jobs)
     


       Strong ability to select, apply algorithms and data structures appropriate for processing large data sets
     





     Nice to Have Skills and Experience:
   





 Experience with Python, including experience with frameworks (such as FastAPI), libraries (such as SQLAlchemy and pandas), and core programming concepts such as OOP, SOLID, dependency injection, unit testing, optimization, etc.



 Experience with multiple IAC (Infrastructure as Code) Tools such as Terraform, Cloudformation, AWS CDK



 Experience in CI/CD pipelines, ideally CircleCI



 Experience in NoSQL Databases (Snowflake, DynamoDB, MongoDB, etc.)



 Experience with Automated Testing/TDD and QA frameworks is a plus



 Experience with HIPAA security guidelines & compliance is a plus






       About Progyny:
     



       Progyny is a transformative fertility, family building and women’s health benefits solution, trusted by the nation’s leading employers, health plans and benefits purchasers. We envision a world where everyone can realize dreams of family and ideal health. Our outcomes prove that comprehensive, inclusive and intentionally designed solutions simultaneously benefit employers, patients and physicians.
     

       Our benefits solution empowers patients with concierge support, coaching, education, and digital tools; provides access to a premier network of fertility and women's health specialists who use the latest science and technologies; drives optimal clinical outcomes; and reduces healthcare costs.
     

       Our mission is to empower healthier, supported journeys through transformative fertility, family building and women’s health benefits.
     


       Headquartered in New York City, Progyny has been recognized for its leadership and growth. Come join a company that has been recognized by CNBC Disruptor 50, Modern Healthcare’s Best Places to Work in Healthcare, Forbes’ Best Employers, Financial Times, INC. 5000, Inc Power Partners and Crain’s Fast 50 for NYC.
     




 Our perks:
     



         Family friendly benefits: Paid family and parental leave-, fertility and family building benefits (including egg freezing, IVF, and adoption support), family care fund and Parents’ Employee Resource Group
       


         Health, dental, vision and life insurance options for employees and family
       


         Free in-person, virtual and text-based mental health and wellness support
       


         Paid time off, including vacation, sick leave, personal days and summer flex time
       


         Company equity
       


         Bonus program
       


         401(k) plan with company match
       


         Access to on-demand legal and financial advice
       


         Company social events
       


         Flex days (3 days a week in the office) and onsite meals and snacks for employees reporting into our NY office
       





       In compliance with New York City's Wage Transparency Law, the annual salary [wage] range for NYC-based applicants is: $160,000 - $185,000. There are a variety of factors that go into determining a salary range, including but not limited to external market benchmark data, geographic location, and years of experience sought/required. Progyny offers a total compensation package comprised of base salary, cash bonus, and equity.
     


       Progyny is proud to be an Equal Opportunity and Affirmative Action employer. We respect and seek to empower each individual and support the diverse cultures, perspectives, skills and experiences within our workforce. All qualified applicants will receive consideration for employment without regard to race, creed, color, religion, sex, sexual orientation, gender identity or expression, national origin, disability, age, genetic information, marital status, pregnancy or related condition, status as a protected veteran, criminal history consistent with legal requirements or any other basis protected by law.
     


       If you are an individual with a disability and need assistance or an accommodation during the recruiting process, please send an e-mail to 
      
       apply@progyny.com
      .
'''
doc = nlp2(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
print("done")